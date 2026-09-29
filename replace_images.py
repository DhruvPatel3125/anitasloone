import os
import re

file_path = r"e:\Downloads\saloon\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace .jpg.jpg with .webp
new_content = re.sub(r'\.jpg\.jpg', '.webp', content, flags=re.IGNORECASE)
# Replace .jpg with .webp
new_content = re.sub(r'\.jpg', '.webp', new_content, flags=re.IGNORECASE)
# Replace .png with .webp
new_content = re.sub(r'\.png', '.webp', new_content, flags=re.IGNORECASE)

if content != new_content:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Replacements made.")
else:
    print("No replacements needed.")
