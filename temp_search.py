
with open('static/assets/main/index.68ff6.js', 'r', encoding='utf-8') as f:
    content = f.read()
    results = []
    start_pos = 0
    while True:
        target = 'this.scheduleOnce(function() {k.ServerAddrInfo.getInstance().requestPCServer();}, 2);'
        index = content.find(target, start_pos)
        if index == -1:
            break
        
        print(f"Found at index: {index}")
        start_pos = index + 1
