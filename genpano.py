import requests
import sys
from PIL import Image

request = True

zoom = 2

imageNames = []

if request:
    for y in range(2):
        for x in range(4):
            panoid = "VX3mphoAvoTu1w_baueRkg"
            url = f"https://streetviewpixels-pa.googleapis.com/v1/tile?cb_client=maps_sv.tactile&panoid={panoid}&x={x}&y={y}&zoom={zoom}&nbt=1&fover=2"
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                "cache-control": "max-age=0",
                "priority": "u=0, i",
                "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                "sec-ch-ua-arch": '"x86"',
                "sec-ch-ua-bitness": '"64"',
                "sec-ch-ua-full-version-list": '"Google Chrome";v="125.0.6422.114", "Chromium";v="125.0.6422.114", "Not.A/Brand";v="24.0.0.0"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-model": '""',
                "sec-ch-ua-platform": '"Windows"',
                "sec-ch-ua-platform-version": '"15.0.0"',
                "sec-ch-ua-wow64": "?0",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            }
            res = requests.get(url, headers=headers)
            outfile = f"x{x}-y{y}.jpg"
            imageNames.append(outfile)
            with open(outfile, "wb") as file:
                file.write(res.content)


images = [Image.open(x) for x in imageNames]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths) // 2
total_height = heights[0] * 2
# max_height = max(heights)

new = Image.new("RGB", (total_width, total_height))

x_offset = 0
y_offset = 0
i = 0
for im in images:
    new.paste(im, (x_offset, y_offset))
    x_offset += im.size[0]
    i += 1
    if i == 4:
        y_offset += im.size[1]
        x_offset = 0

new.save("combined.jpg")

# https://www.google.ca/maps/@43.8899151,-79.4079582,3a,75y,227.89h,58.7t/data=!3m7!1e1!3m5!1skJoLkX3bQNwFsu_AlvT_Ag!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DkJoLkX3bQNwFsu_AlvT_Ag%26cb_client%3Dmaps_sv.share%26w%3D900%26h%3D600%26yaw%3D227.8895510601895%26pitch%3D31.301861552949447%26thumbfov%3D90!7i16384!8i8192?coh=205410&entry=ttu
# https://streetviewpixels-pa.googleapis.com/v1/tile?cb_client=maps_sv.tactile&panoid=kJoLkX3bQNwFsu_AlvT_Ag&x=0&y=7&zoom=4&nbt=1&fover=2
# https://streetviewpixels-pa.googleapis.com/v1/tile?cb_client=maps_sv.tactile&panoid=YuTzaTyLM-hE8haDcrRLsw&x={x}&y={y}&zoom={zoom}&nbt=1&fover=2
