import zlib, struct

path = r'C:/Users/julio/.gemini/antigravity/brain/9c9688a8-12d0-40e5-b617-f3beeb1dc998/.user_uploaded/media_1795038533880_2b743922.png'

with open(path, 'rb') as f:
    f.read(8) # PNG signature
    idat = b''
    w, h = 0, 0
    while True:
        chunk = f.read(8)
        if not chunk or len(chunk) < 8:
            break
        length, ctype = struct.unpack('>I4s', chunk)
        data = f.read(length)
        f.read(4) # crc
        if ctype == b'IHDR':
            w, h, bitdepth, colortype, comp, filt, inter = struct.unpack('>IIBBBBB', data)
            print(f"IHDR: {w}x{h}, depth={bitdepth}, colortype={colortype}")
        elif ctype == b'IDAT':
            idat += data
        elif ctype == b'IEND':
            break

raw = zlib.decompress(idat)
print(f"Decompressed {len(raw)} bytes")

# colortype 2 is RGB (3 bytes per pixel), 6 is RGBA (4 bytes per pixel)
bpp = 3 if colortype == 2 else 4
stride = 1 + w * bpp

colors = []
for y in range(0, h, 10):
    row = raw[y*stride + 1 : (y+1)*stride]
    for x in range(0, w, 20):
        px = row[x*bpp : x*bpp + 3]
        r, g, b = px[0], px[1], px[2]
        colors.append((r, g, b))

hexes = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in colors]
from collections import Counter
counts = Counter(hexes).most_common(10)
print("Top colors:")
for hex_val, count in counts:
    print(f"  {hex_val}: {count}")

# Sample min/max
r_vals = [c[0] for c in colors]
g_vals = [c[1] for c in colors]
b_vals = [c[2] for c in colors]
print(f"R range: {min(r_vals)} - {max(r_vals)}")
print(f"G range: {min(g_vals)} - {max(g_vals)}")
print(f"B range: {min(b_vals)} - {max(b_vals)}")
