from .config import USE_TESTNET

class MockClient:
    def futures_create_order(self, **kwargs):
        return {
            "orderId": 123456789,
            "status": "FILLED",
            "executedQty": kwargs.get("quantity"),
            "avgPrice": kwargs.get("price", "MARKET_PRICE"),
            "symbol": kwargs.get("symbol"),
            "side": kwargs.get("side"),
            "type": kwargs.get("type")
        }

def get_client():
    if USE_TESTNET:
        from binance.client import Client
        import os
        from dotenv import load_dotenv

        load_dotenv()
        client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_API_SECRET")
        )
        client.FUTURES_URL = "https://testnet.binancefuture.com"
        return client
    else:
        return MockClient()
