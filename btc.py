from locale import currency
import requests
currency = "usd"
coinsList = None

def getCoinsList():
    global coinsList
    #{'id': '01coin', 'symbol': 'zoc', 'name': '01coin', 'platforms': {}}
    response =  requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if response.ok ==True:
        print("response ok")
        data = response.json()
        #print(data[0])
        print("Ilość śledzonych crypto: " + str(len(data)))
        coinsList = data
def findCoinBySymbol(symbol):
    symbol = symbol.lower().strip()
    for coin in coinsList:
        if coin ["symbol"] == symbol:
            return coin
    else:
        return None


def getCoinLastMarketData(coinId):
    #{'bitcoin': {'pln': 90152, 'pln_market_cap': 1727063580278.9695, 'pln_24h_vol': 204685028699.7084, 'pln_24h_change': 0.3561577757352101, 'last_updated_at': 1663812126}}
    response =requests.get("https://api.coingecko.com/api/v3/simple/price?ids="+ coinId +"&vs_currencies="+ currency +"&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")
    if response.ok:
        data =response.json()
        return data
    else:
        return None


def getCoinPriceInCurrency(coinId, currency):
    currency = currency.lower().strip()
    marketData = getCoinLastMarketData(coinId)
    return marketData[coinId][currency]



getCoinsList()

btcData =  findCoinBySymbol("BTC")
#print(btcData)
marketData = getCoinLastMarketData(btcData["id"])
#print("marketData: " , marketData)

coinPrice = getCoinPriceInCurrency(btcData["id"], currency)
print("Btc price in: " + currency, coinPrice)

print("\nCrypto exchange")

while True:
    crytoSymbolToBuy = input("Wybierz symbol krypto do kupienia (np. btc) lub exit aby zakończyć: ")
    if crytoSymbolToBuy == "exit": break

    coinData = findCoinBySymbol(crytoSymbolToBuy)
    if coinData == None:
        print("Nie ma takiego crypto")
        if crytoSymbolToBuy == "exit": break
        continue
    coinPrice = getCoinPriceInCurrency(coinData["id"], currency)
    print("Cena: " + str(coinData["id"]), coinPrice, currency)

    moneyToBuyCrypto = float(input("Ile usd chcesz wydać?: "))
    
    boughtCrypto = moneyToBuyCrypto / coinPrice

    print("\nJesteś w stanie kupić: " +str(boughtCrypto) + " " + crytoSymbolToBuy)
