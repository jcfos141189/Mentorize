import os
import re

with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\design-system.html', 'r', encoding='utf-8') as f:
    text = f.read()

classes = [
    'framer-XNIeN',
    'framer-nilurh',
    'framer-1vtt1px',
    'framer-qv6cy6',
    'framer-18pkf2p',
    'framer-pa691l',
    'framer-3pkuos',
    'framer-179r1kf',
    'framer-1ru8xec',
    'framer-aq0gsr',
    'framer-v-77o094',
    'framer-um6n2o',
    'framer-r8vf06'
]

for c in classes:
    matches = re.findall(rf'(\.{c}[^{{]*\{{[^}}]+\}})', text)
    print(f"=== CSS for {c} ({len(matches)} matches) ===")
    for m in matches[:3]:
        print(m[:250])
