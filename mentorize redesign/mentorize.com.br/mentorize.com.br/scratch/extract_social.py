import os
import re

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'hanzo_footer_sample.html'), 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Social Links')
if pos != -1:
    sub = html[pos:pos+4000]
    print(sub)
else:
    print("Social Links not found in html snippet")
