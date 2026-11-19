import os

for root, dirs, files in os.walk(r'c:\Users\julio\OneDrive\Desktop'):
    for f in files:
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.avif', '.webp')):
            full = os.path.join(root, f)
            sz = os.path.getsize(full)
            if sz == 53847 or 'bg' in f.lower() or 'header' in f.lower():
                print(f"{sz} bytes: {full}")
