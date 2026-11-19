import os, re

path = r'C:\Users\julio\.gemini\antigravity\brain\9c9688a8-12d0-40e5-b617-f3beeb1dc998\scratch\mentorize_decoded.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('footer')
if pos != -1:
    print(text[pos-200:pos+2500])
else:
    print("footer tag not found")
