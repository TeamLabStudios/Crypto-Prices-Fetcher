import requests

def get_crypto_prices(cryptos):
    """Obtiene los precios actuales de criptomonedas."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ','.join(cryptos),
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

if __name__ == "__main__":
    # Lista de criptomonedas populares
    cryptocurrencies = [
        'bitcoin', 'ethereum', 'ripple', 'litecoin', 'cardano',
        'dogecoin', 'polkadot', 'binancecoin', 'solana', 'chainlink',
        'stellar', 'monero', 'vechain', 'tron', 'cosmos',
        'tezos', 'avalanche-2', 'theta-token', 'uniswap', 'aave'
    ]

    prices = get_crypto_prices(cryptocurrencies)
    if prices:
        for crypto, price_info in prices.items():
            print(f"The current price of {crypto.capitalize()} is ${price_info['usd']} USD")