import os

file_path = 'static/assets/main/index.68ff6.js'

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit(1)

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 尝试替换两种格式的判断条件
targets = [
    'if (y.GamePlatform.isPC() || y.GamePlatform.isAndroid())',
    'if(y.GamePlatform.isPC()||y.GamePlatform.isAndroid())'
]

replaced = False
for target in targets:
    if target in content:
        content = content.replace(target, 'if (true)')
        replaced = True
        print(f"Replaced: {target}")

if replaced:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully patched index.68ff6.js")
else:
    print("Target string not found in index.68ff6.js")
