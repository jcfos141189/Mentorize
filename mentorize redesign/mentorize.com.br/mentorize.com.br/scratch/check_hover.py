with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\assets\catalog\framer-ssr.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'([^{}]*framer-r8vf06[^{}]*\{[^}]+\})', css)
for m in matches:
    print(m)

matches2 = re.findall(r'([^{}]*framer-fdi9yo[^{}]*\{[^}]+\})', css)
for m in matches2:
    print(m)

matches3 = re.findall(r'([^{}]*framer-12unp5g[^{}]*\{[^}]+\})', css)
for m in matches3:
    print(m)
