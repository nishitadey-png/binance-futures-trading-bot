from .validators import validate_order

def place_order(client, logger, symbol, side, order_type, quantity, price=None):
    validate_order(symbol, side, order_type, quantity, price)

    logger.info("Order request received")
    logger.info(
        f"Symbol={symbol}, Side={side}, Type={order_type}, "
        f"Quantity={quantity}, Price={price}"
    )

    try:
        order = client.create_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        logger.info("Order executed successfully")
        logger.info(f"Order response: {order}")

        return order

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        raise
