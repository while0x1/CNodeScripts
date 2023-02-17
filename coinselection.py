mintPricePlusFee = 53500000
collateralCost = 5000000

def findBuyUtxo(utxoList,mintPricePlusFee,):
    mintUtxoList = []
    for n in utxoList:
        if int(n['lovelace']) >= mintPricePlusFee:
            mintUtxoList.append(n)
    if len(mintUtxoList) > 0:
        min = mintUtxoList[0] 
    else:
        return 'NoUtxos'
    for i in mintUtxoList:
            if int(i['lovelace']) < int(min['lovelace']):
                min = i
    return min
#End

def findCollateralUtxo(utxoList,buyUtxo):
    colUtxoList = []
    buyTxId = buyUtxo['txhash'] + buyUtxo['txid']
    for n in utxoList:
        if int(n['lovelace']) >= 5000000:
            colTxId = n['txhash'] + n['txid']
            if colTxId != buyTxId:
                colUtxoList.append(n)
    if len(colUtxoList) > 0:
        min = colUtxoList[0] 
    else:
        return 'NoUtxos'
    for i in colUtxoList:
            if int(i['lovelace']) < int(min['lovelace']):
                min = i
    return min
