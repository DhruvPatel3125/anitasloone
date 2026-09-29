import re

with open(r"e:\Downloads\saloon\index.html", "r", encoding="utf-8") as f:
    content = f.read()

imgs = re.findall(r'<img[^>]+>', content)
for i, img in enumerate(imgs):
    print(f"Img {i}: {img}")
