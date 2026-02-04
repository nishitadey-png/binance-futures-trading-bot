import uuid
import time

class MockFuturesClient:
    def futures_create_order(self, **kwargs):
        time.sleep(0.5)  # simulate network delay

        return {
            "orderId": str(uuid.uuid4()),
            "symbol": kwargs.get("symbol"),
            "side": kwargs.get("side"),
            "type": kwargs.get("type"),
            "status": "FILLED",
            "executedQty": kwargs.get("quantity"),
            "avgPrice": kwargs.get("price", "MARKET_PRICE"),
            "timestamp": int(time.time() * 1000)
        }

def get_client():
    return MockFuturesClient()
