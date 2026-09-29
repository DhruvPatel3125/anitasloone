with open('e:/Downloads/saloon/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

count = text.count('marquee-strip')
print(f'Count: {count}')
