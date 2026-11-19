import os
import re

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'hanzo_footer_sample.html'), 'r', encoding='utf-8') as f:
    html = f.read()

print("=== REMAINING TAGS IN FOOTER ===")
tags = re.findall(r'<([a-zA-Z0-9]+)\s+([^>]+)>', html)
for i, (tag, attrs) in enumerate(tags[40:]):
    name = re.search(r'data-framer-name="([^"]+)"', attrs)
    cls = re.search(r'class="([^"]+)"', attrs)
    style = re.search(r'style="([^"]+)"', attrs)
    name_str = f" [name={name.group(1)}]" if name else ""
    cls_str = f" [cls={cls.group(1)}]" if cls else ""
    style_str = f" [style={style.group(1)[:60]}...]" if style else ""
    print(f"{i+40}: <{tag}>{name_str}{cls_str}{style_str}")
