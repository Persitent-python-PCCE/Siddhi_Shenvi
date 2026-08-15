class Order:

    def __init__(self, order_id, user_id, total_amount, status):
        self.order_id = order_id
        self.user_id = user_id
        self.total_amount = total_amount
        self.status = status

class OrderItem:

    def __init__(self, order_item_id,order_id, product_id, quantity, price, subtotal):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.subtotal = subtotal