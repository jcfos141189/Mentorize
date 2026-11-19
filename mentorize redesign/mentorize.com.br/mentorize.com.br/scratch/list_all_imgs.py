with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\assets\overview\assets\hanzo.framer.website\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', text)
print(f"Total img tags: {len(imgs)}")
for i, src in enumerate(imgs):
    # print context of each img
    pos = text.find(src)
    parent = text[max(0, pos-200):min(len(text), pos+300)]
    framer_name = re.search(r'data-framer-name="([^"]+)"', parent)
    name = framer_name.group(1) if framer_name else 'unknown'
    print(f"{i}: {name} -> {src}")
