mintPricePlusFee = 53500000
collateralCost = 5000000

def findBuyUtxo(mintPricePlusFee):
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
