import re

path = r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\assets\overview\assets\hanzo.framer.website\index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('framer-3pkuos')
if pos != -1:
    print(text[pos:pos+4000])
