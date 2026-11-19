import re

path = r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\assets\catalog\framer-ssr.css'
with open(path, 'r', encoding='utf-8') as f:
    css = f.read()

keyframes = re.findall(r'@keyframes[^{]+{[^}]+(?:{[^}]+})*[^}]+}', css)
print(f"Found {len(keyframes)} keyframes in framer-ssr.css:")
for k in keyframes:
    name = re.match(r'@keyframes\s+([a-zA-Z0-9_-]+)', k)
    if name:
        print("  Keyframe:", name.group(1))
