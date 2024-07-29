import numpy as np
import pandas as pd
import torch
import os
from PIL import Image
from torch.utils.data import Dataset
from torchvision.io import read_image


df = pd.read_csv("./archive/images_with_countries.csv")
df["date_taken"] = pd.to_datetime(df["date_taken"], format=f"%Y-%m-%d")
# filtered = df[df["date_taken"] > "2021-01-01"]

# canadian = df[df["country"] == "Montenegro"]

countries = sorted(df["country"].unique())
country_cnt = len(countries)

countries_df = pd.DataFrame(
    countries, columns=["country"], index=range(0, len(countries))
)


dct = countries_df["country"].to_dict()

reversed = {v: k for k, v in dct.items()}

df["country_id"] = df["country"].map(reversed)

# df["img_name"] = df["id"].astype(str) + ".jpeg"

# annotated = df[["img_name", "country_id"]].copy()
# annotated.to_csv("./annotations.csv", index=False)

# one_hot = torch.nn.functional.one_hot(torch.tensor(list(range(0, len(countries)))))


# dataset = list(map(lambda x, y: (x, one_hot[y]), df["id"], df["country_id"]))
# data_df = pd.DataFrame(dataset, columns=["img_id", "target"])
# print(dataset[0], len(dataset[0][1]))


class ImageDataset(Dataset):
    def __init__(
        self,
        annotations_file,
        img_dir,
        transform=None,
        target_transform=None,
        device="cpu",
    ):
        super(ImageDataset, self).__init__()
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform
        self.device = device

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = Image.open(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        # image.to(self.device)
        label = torch.tensor(label)
        # label.to(self.device)
        # print(image)
        # print(label)
        return image, label


# goal - dataset that loads image id along with a one hot vector for the correct class


# print(df.head())


# print(df.head())
