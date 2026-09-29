import re

with open(r"e:\Downloads\saloon\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Function to add decoding="async" to img tags if not present
def add_decoding(match):
    img_tag = match.group(0)
    if 'decoding=' not in img_tag:
        # Insert decoding="async" before the closing bracket
        # Handle trailing slash if present
        if img_tag.endswith('/>'):
            return img_tag[:-2] + ' decoding="async" />'
        elif img_tag.endswith('>'):
            return img_tag[:-1] + ' decoding="async">'
    return img_tag

new_content = re.sub(r'<img[^>]+>', add_decoding, content)

with open(r"e:\Downloads\saloon\index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Added decoding='async' to images.")
