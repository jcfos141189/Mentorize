import re

with open(r'c:\Users\julio\OneDrive\Desktop\hanzo-design-system\hanzo-design-system\assets\overview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length of overview/index.html:', len(text))
pos = text.find('footer')
print('First footer index:', pos)
if pos != -1:
    print(text[pos-200:pos+1500])
