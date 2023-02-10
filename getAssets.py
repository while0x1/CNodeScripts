def findassets():
    assetdict = []
    cmd = ["cardano-cli", "query", "utxo", "--address", paymentaddr, "--testnet-magic", "1"]
    rs = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    if len(rs.stderr) < 1:
        lines = rs.stdout.splitlines()
        if len(lines) > 2:
            for l in lines:
                assetcount = l.count(".") 
                if assetcount > 0:
                    assetdict.append(l)
    if len(assetdict) > 0:
        for a in assetdict:
            print(a)
