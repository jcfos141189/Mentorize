import os

here = os.path.dirname(os.path.abspath(__file__))
with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\design-system.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('data-framer-name="footer"')
if pos != -1:
    sub = text[pos-200:pos+25000]
    out_path = os.path.join(here, 'hanzo_footer_sample.html')
    with open(out_path, 'w', encoding='utf-8') as out:
        out.write(sub)
    print("Found and saved", len(sub), "characters from footer to", out_path)
else:
    print("Not found")
