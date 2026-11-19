import os
import struct

path = r'C:/Users/julio/.gemini/antigravity/brain/9c9688a8-12d0-40e5-b617-f3beeb1dc998/.user_uploaded/media_1795038533880_2b743922.png'
with open(path, 'rb') as f:
    header = f.read(24)
    w, h = struct.unpack('>LL', header[16:24])
    print(f"PNG size: {w}x{h}")
print("File size:", os.path.getsize(path))
