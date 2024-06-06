import numpy as np
import pandas as pd
import reverse_geocode

df = pd.read_csv("./archive/images.csv")

df["date_taken"] = pd.to_datetime(df["date_taken"], format="%Y-%m")


filtered = df[df["date_taken"] > "2021-01-01"]

# print(zip(filtered["lat"], filtered["lng"]))
coords = list(zip(filtered["lat"], filtered["lng"]))
print(coords[0:3])
# countries = reverse_geocode.search(coords[0])
x = 36.988287
y = 35.272027
coordinates = [(x, y)]

# coordinates = (-37.81, 144.96), (31.76, 35.21)
# reverse_geocode.search(coordinates)
print(reverse_geocode.search(coordinates))

# print(countries[0])
# print(filtered.info())
