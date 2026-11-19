with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\design-system.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('<iframe')
if pos != -1:
    print(text[pos:pos+300])
