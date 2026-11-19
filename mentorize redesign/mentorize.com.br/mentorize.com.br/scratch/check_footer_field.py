with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\design-system.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for spec in ['Footer field', 'Footer', 'Light sweep', 'Dark frame']:
    pos = text.find(f'<h3>{spec}</h3>')
    if pos != -1:
        print(f"=== SPEC: {spec} ===")
        print(text[pos:pos+1500])
