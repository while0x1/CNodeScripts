def getTip():  
    command = ["cardano-cli", "query", "tip", "--testnet-magic", "1"]
    rs = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    if len(rs.stderr) == 0:
        js = json.loads(rs.stdout)
        blockno = js['block']
        slotno = js['slot']
        hash = js['hash']
        for k, v in js.items():
            print(k, v)

getTip()
