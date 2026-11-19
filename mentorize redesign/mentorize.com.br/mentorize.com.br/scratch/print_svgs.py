import os
import re

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'hanzo_footer_sample.html'), 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Social Links')
if pos != -1:
    links = re.findall(r'<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html[pos:], re.DOTALL)
    for i, (href, inner) in enumerate(links):
        svg_m = re.search(r'<svg[^>]*viewBox="([^"]+)"[^>]*>(.*?)</svg>', inner, re.DOTALL)
        if svg_m:
            vb = svg_m.group(1)
            content = svg_m.group(2)
            print(f"=== ICON {i+1}: {href} (viewBox={vb}) ===")
            print(content.strip())
