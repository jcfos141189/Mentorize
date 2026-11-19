import re

with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\design-system.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for image or scroll in design-system.html
matches = re.findall(r'(\.[a-zA-Z0-9_-]+\s*\{[^}]*image[^}]*\})', text)
for m in matches[:10]:
    print('IMG RULE:', m[:150])

# Let's check sections near the end of design-system.html
specs = re.findall(r'<div class="ds-spec\s*"><h3>([^<]+)</h3>', text)
print('All specs:', specs)
