with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\assets\catalog\framer-ssr.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'([^{}]*framer-qp6ulc[^{}]*\{[^}]+\})', css)
for m in matches:
    print(m)
