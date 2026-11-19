with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\assets\overview\assets\hanzo.framer.website\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('data-framer-name="footer"')
print("Footer found at:", pos)
if pos != -1:
    sub = text[pos-1000:pos+3000]
    print("--- SURROUNDING HTML ---")
    print(sub)
