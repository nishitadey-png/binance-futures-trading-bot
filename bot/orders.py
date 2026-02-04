from .validators import validate_order

def place_order(client, logger, symbol, side, order_type, quantity, price=None):
    validate_order(symbol, side, order_type, quantity, price)

    logger.info(
        f"Placing order | Symbol={symbol} Side={side} "
        f"Type={order_type} Qty={quantity} Price={price}"
    )

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            price=price
        )

        logger.info(f"Order response: {order}")
        return order

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        raise
