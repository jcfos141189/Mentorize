with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\assets\overview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script[^>]*>(.*?)</script>', text, re.DOTALL)
print('Found scripts count:', len(scripts))
for i, s in enumerate(scripts):
    print(f'Script {i} length:', len(s))
    if len(s) < 500:
        print(s)
