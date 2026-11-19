import os
import re

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'hanzo_footer_sample.html'), 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Social Links')
if pos != -1:
    links = re.findall(r'<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html[pos:], re.DOTALL)
    print(f"Found {len(links)} links in Social Links:")
    for href, inner in links:
        print("HREF:", href)
        svgs = re.findall(r'<svg[^>]*>(.*?)</svg>', inner, re.DOTALL)
        print(f"  SVGs count: {len(svgs)}")
        for s in svgs[:1]:
            paths = re.findall(r'<path[^>]*d="([^"]+)"', s)
            for p in paths:
                print("  PATH:", p[:60], "...")
