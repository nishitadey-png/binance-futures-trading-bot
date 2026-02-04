import uuid
from datetime import datetime

class MockClient:
    def create_order(self, symbol, side, order_type, quantity, price=None):
        return {
            "orderId": str(uuid.uuid4())[:8],
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "price": price,
            "status": "FILLED",
            "executedQty": quantity,
            "avgPrice": price if price else "MARKET_PRICE",
            "timestamp": datetime.utcnow().isoformat()
        }

def get_client():
    return MockClient()
