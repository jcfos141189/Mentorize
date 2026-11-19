import re

css_path = r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\assets\catalog\framer-ssr.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

classes = [
    'framer-XNIeN',
    'framer-nilurh',
    'framer-1vtt1px',
    'framer-qv6cy6',
    'framer-18pkf2p',
    'framer-pa691l',
    'framer-3pkuos',
    'framer-179r1kf',
    'framer-divrc2',
    'framer-wz2oom',
    'framer-1ru8xec',
    'framer-aq0gsr',
    'framer-v-77o094',
    'framer-um6n2o',
    'framer-kcb4pg'
]

for c in classes:
    matches = re.findall(rf'([^{{}}]*\.{c}[^{{}}]*\{{[^}}]+\}})', css)
    print(f"=== {c} in framer-ssr.css ({len(matches)} rules) ===")
    for m in matches[:4]:
        print(m.strip())
