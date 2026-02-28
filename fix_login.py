
file_path = 'static/assets/main/index.68ff6.js'
target = 'this.scheduleOnce(function() {k.ServerAddrInfo.getInstance().requestPCServer();}, 2);'
replacement = 'var self=this;this.scheduleOnce(function() {k.ServerAddrInfo.getInstance().requestPCServer(self.account);}, 2);'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

if target in content:
    new_content = content.replace(target, replacement)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("File updated successfully.")
else:
    print("Target string not found.")
