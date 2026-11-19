import re

path = r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\assets\overview\assets\hanzo.framer.website\index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'class="[^"]*framer-74s1wo[^"]*"', text)]
for idx in matches:
    print(text[idx-50:idx+350])
