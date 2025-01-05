# 🚀 Crypto Price Tracker

Un script simple pero potente para monitorear los precios en tiempo real de las principales criptomonedas utilizando la API de CoinGecko.

## 📋 Descripción

Este proyecto proporciona una herramienta para obtener los precios actuales de múltiples criptomonedas en dólares estadounidenses (USD). Utiliza la API pública de CoinGecko para obtener datos precisos y actualizados de 20 criptomonedas populares, incluyendo Bitcoin, Ethereum, y otras altcoins importantes.

## 🔧 Requisitos previos

- Python 3.6 o superior
- Biblioteca `requests`

## ⚙️ Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/TeamLabStudios/Crypto-Prices-Fetcher.git
cd crypto-price-tracker
```

2. Instala las dependencias necesarias:
```bash
pip install requests
```

## 🚀 Uso

Para ejecutar el script, simplemente usa:
```bash
python crypto_tracker.py
```

El script mostrará los precios actuales de las siguientes criptomonedas:
- Bitcoin
- Ethereum
- Ripple
- Litecoin
- Cardano
- Dogecoin
- Polkadot
- Binance Coin
- Solana
- Chainlink
- Stellar
- Monero
- VeChain
- TRON
- Cosmos
- Tezos
- Avalanche
- Theta
- Uniswap
- Aave

## 🛠️ Funcionalidades

- Obtención de precios en tiempo real
- Soporte para múltiples criptomonedas
- Manejo de errores de API
- Formateo automático de nombres de criptomonedas
- Conversión a USD

## 📈 Ejemplo de salida

```
The current price of Bitcoin is $45000 USD
The current price of Ethereum is $3000 USD
...
```

## 🔄 API

El proyecto utiliza la siguiente función principal:

```python
def get_crypto_prices(cryptos):
    """
    Obtiene los precios actuales de criptomonedas.
    
    Args:
        cryptos (list): Lista de identificadores de criptomonedas
        
    Returns:
        dict: Diccionario con los precios de las criptomonedas en USD
    """
```

## 📝 Notas

- La API de CoinGecko tiene límites de tasa. Para uso intensivo, considera registrarte para obtener una API key.
- Los precios se actualizan en tiempo real cada vez que se ejecuta el script.
- Los identificadores de las criptomonedas deben coincidir con los utilizados por CoinGecko.

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.

## ✍️ Autor

TeamLabStudios
- GitHub: [@TeamLabStudios](https://github.com/TeamLabStudios)


## 🙏 Agradecimientos

- CoinGecko por proporcionar una API gratuita y confiable
- A la comunidad de Python por las herramientas y bibliotecas utilizadas
