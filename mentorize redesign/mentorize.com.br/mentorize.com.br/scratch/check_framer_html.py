import re

path = r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\assets\overview\assets\hanzo.framer.website\index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('nilurh')
if pos != -1:
    print("Found nilurh in hanzo.framer.website:")
    print(text[max(0, pos-200):min(len(text), pos+800)])
else:
    print("nilurh not found")

pos2 = text.find('framer-XNIeN')
if pos2 != -1:
    print("Found framer-XNIeN:")
    print(text[max(0, pos2-200):min(len(text), pos2+800)])
