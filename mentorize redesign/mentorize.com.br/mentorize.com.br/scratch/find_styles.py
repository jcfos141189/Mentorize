import re

with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\design-system.html', 'r', encoding='utf-8') as f:
    text = f.read()

styles = re.findall(r'<style[^>]*>(.*?)</style>', text, re.DOTALL)
print(f"Found {len(styles)} style tags")
for i, s in enumerate(styles):
    for c in ['1vtt1px', 'nilurh', '1ru8xec', 'aq0gsr', 'um6n2o', 'divrc2', 'wz2oom']:
        if c in s:
            print(f"Found {c} in style tag {i}")
            # print surrounding CSS
            idx = s.find(c)
            print(s[max(0, idx-100):min(len(s), idx+400)])
            print("-------------------")
