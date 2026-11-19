import re

path = r'C:\Users\julio\.gemini\antigravity\brain\9c9688a8-12d0-40e5-b617-f3beeb1dc998\scratch\mentorize_decoded.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('contato@mentorize.com.br')
if pos != -1:
    print(text[pos-400:pos+600])
