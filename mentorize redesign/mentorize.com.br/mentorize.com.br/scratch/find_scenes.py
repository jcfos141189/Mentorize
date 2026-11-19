import re

with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\design-system.html', 'r', encoding='utf-8') as f:
    text = f.read()

scenes = re.findall(r'data-scene="([^"]+)"', text)
print('Scenes found in DS:', scenes)

specs = re.findall(r'<div class="ds-spec\s*"><h3>([^<]+)</h3>(.*?)</div>\s*</div>', text, re.DOTALL)
for title, content in specs:
    print('SPEC TITLE:', title.strip())
    # find images or descriptions
    meta = re.findall(r'class="ds-meta">([^<]+)<', content)
    if meta:
        print('  Meta:', meta)

scripts = re.findall(r'<script>(.*?)</script>', text, re.DOTALL)
for i, s in enumerate(scripts):
    print(f'Script {i} length:', len(s))
    lines = [line.strip() for line in s.split('\n') if any(w in line.lower() for w in ['scroll', 'parallax', 'scene', 'footer', 'reveal'])]
    for l in lines[:20]:
        print('   ', l[:120])
