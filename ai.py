import timm.data
import torch.utils
from data import country_cnt, ImageDataset
import os
from PIL import Image, ImageOps
from tqdm import tqdm
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from transformers import ViTImageProcessor, Trainer
import timm
from torchvision.transforms import v2, InterpolationMode


if torch.cuda.is_available():
    device_name = "cuda"
elif torch.backends.mps.is_available():
    device_name = "mps"
else:
    device_name = "cpu"
device = torch.device(device_name)

# transform = transforms.Compose(
#     [transforms.ToTensor()]
# )  # not normalizing because I suspect colour might matter


# ViTImageProcessor.from_pretrained()

# print(torch.nn.functional.one_hot(torch.tensor(0), country_cnt))


batch_size = 3

model = timm.create_model(
    "tiny_vit_21m_512.dist_in22k_ft_in1k",
    pretrained=True,
    num_classes=0,  # remove classifier nn.Linear
)
model = model.eval()

model.to(device)

data_config = timm.data.resolve_model_data_config(model)
transforms = v2.Compose(
    [
        v2.Resize(
            size=(512, 512),
            interpolation=InterpolationMode.BICUBIC,
            max_size=None,
            antialias=True,
        ),
        v2.CenterCrop(size=(512, 512)),
        v2.ToImage(),
        v2.Normalize(
            mean=torch.tensor([0.4850, 0.4560, 0.4060]),
            std=torch.tensor([0.2290, 0.2240, 0.2250]),
        ),
    ]
)
transforms = timm.data.create_transform(**data_config, is_training=False)


ds = ImageDataset(
    "./annotations.csv",
    "./archive/images",
    transforms,
    # lambda x: torch.nn.functional.one_hot(torch.tensor(x), country_cnt),
    None,
)

dl = torch.utils.data.DataLoader(ds, batch_size=batch_size, shuffle=True)

print("using ", device)


def learn(net, dl, epochs=100):
    model.train()
    optim = torch.optim.Adam(net.parameters(), lr=5e-5)
    loss_fcn = nn.CrossEntropyLoss()
    losses = []
    numBatches = len(ds)

    for _ in tqdm(range(epochs)):
        totalLoss = 0

        for img, label in tqdm(dl):
            # img.to(device)
            img = img.to(device)
            label = label.to(device)

            # label.to(device)
            output = model(img)
            loss = loss_fcn(output, label)

            loss.backward()
            optim.step()
            totalLoss += loss.item()
        losses.append(totalLoss / numBatches)
    return losses


loss_history = learn(model, dl, 3)
plt.plot(loss_history)

plt.savefig("./losses.png")


exit()


class CountryClassify(nn.Module):
    """
    net = CountryClassify(img_size=28, embedding_dim=3)

    Create a classifier of which country an image was taken in, using vector embedded output from TinyViT model


    Inputs:
      country_dict     dict of country mappings

    Usage:
      net = CountryClassify()
      y = net(x)
    """

    def __init__(self, country_dict: dict):
        self.losses = []
        self.country_cnt = len(country_dict)
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(1000, 512),
            nn.ReLU(),
            nn.Linear(512, 200),
            nn.ReLU(),
            nn.Linear(200, len(country_dict)),
        ).to(device)

        def forward(self, x):
            # x is vector embedding from TinyViT, [1, 1000]
            return self.network(x)


mynet = CountryClassify(dct)


def learn(net, dl, epochs=100):
    mynet.train()
    optim = torch.optim.Adam(mynet.parameters(), lr=0.0001)
    loss_fcn = nn.CrossEntropyLoss()

    for epoch in tqdm(range(epochs)):
        totalLoss = 0

        for inputs, targets in dl:
            inputs = inputs.to(device)
            optim.zero_grad()

            y = net(inputs)
            loss = loss_fcn(y)


# train_dl = torch.utils.data.DataLoader


# def get_image_dimensions(image_path):
#     with Image.open(image_path) as img:
#         return img.size


# def get_all_image_dimensions(folder_path):
#     image_dimensions = []
#     for filename in tqdm(os.listdir(folder_path)):
#         image_path = os.path.join(folder_path, filename)
#         image_dimensions.append(Image.open(image_path).size)
#     return image_dimensions


# folder_path = "./archive/images"
# sizes = pd.DataFrame(get_all_image_dimensions(folder_path), columns=["width", "height"])

# sizes.to_csv("./image-sizes.csv")


# first try training model to see how accurately it can guess countries
# looks like varying heights can be fixed by cutting off from bottom? ask chatgpt
# notable test try singapore since it only had 16 images

# once it can pretty accurately guess country, see if coordinates can be incorportated in loss function to use both information


def resize_and_pad(image: Image, target_size):
    image.thumbnail(target_size, Image.Resampling.LANCZOS)
    delta_width = target_size[0] - image.width
    delta_height = target_size[1] - image.height
    padding = (
        delta_width // 2,
        delta_height // 2,
        delta_width - (delta_width // 2),
        delta_height - (delta_height // 2),
    )
    return ImageOps.expand(image, padding)
