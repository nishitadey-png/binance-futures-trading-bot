from binance.enums import *
from .validators import validate_order

def place_order(client, logger, symbol, side, order_type, quantity, price=None):
    validate_order(symbol, side, order_type, quantity, price)

    logger.info(
        f"Placing order | Symbol={symbol} Side={side} Type={order_type} Qty={quantity} Price={price}"
    )

    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC
            )

        logger.info(f"Order response: {order}")
        return order

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        raise
