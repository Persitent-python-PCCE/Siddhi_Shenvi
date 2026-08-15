import unittest
from unittest.mock import Mock
from service.order_service import OrderService

class TestOrderManagement(unittest.TestCase):
    def setUp(self):
        self.order_service = OrderService()
        self.order_service.order_dao = Mock()
        self.order_service.cart_dao = Mock()
        self.order_service.product_dao = Mock()

    def test_place_order_valid(self):
        self.order_service.cart_dao.get_cart.return_value = [
            (1, 5, "Laptop", 50000, 2, 100000)
        ]
        self.order_service.product_dao.get_product_by_id.return_value = (5, "Laptop", 50000, 10, 1)
        self.order_service.order_dao.create_order.return_value = 10
        self.order_service.product_dao.update_stock.return_value = 1
        
        result = self.order_service.place_order(1)
        
        self.assertEqual(result, 10)
        self.order_service.cart_dao.clear_cart.assert_called_once_with(1)
        self.order_service.product_dao.update_stock.assert_called_once_with(5, 2)

    def test_place_order_empty_cart(self):
        self.order_service.cart_dao.get_cart.return_value = []
        
        with self.assertRaises(ValueError):
            self.order_service.place_order(1)
            
        self.order_service.order_dao.create_order.assert_not_called()

    def test_insufficient_stock(self):
        self.order_service.cart_dao.get_cart.return_value = [
            (1, 5, "Laptop", 50000, 10, 500000)
        ]
        self.order_service.product_dao.get_product_by_id.return_value = (5, "Laptop", 50000, 5, 1)
        
        with self.assertRaises(ValueError):
            self.order_service.place_order(1)
            
        self.order_service.order_dao.create_order.assert_not_called()

    def test_product_not_found(self):
        self.order_service.cart_dao.get_cart.return_value = [
            (1, 999, "Unknown", 1000, 1, 1000)
        ]
        self.order_service.product_dao.get_product_by_id.return_value = None
        
        with self.assertRaises(ValueError):
            self.order_service.place_order(1)

    def test_get_order_history(self):
        expected_orders = [
            (3, 2500, "PLACED", "2026-08-15 10:00:00"),
            (2, 1500, "PLACED", "2026-08-14 15:30:00")
        ]
        self.order_service.order_dao.get_orders_by_user.return_value = expected_orders
        
        result = self.order_service.get_order_history(1)
        
        self.assertEqual(result, expected_orders)
        self.order_service.order_dao.get_orders_by_user.assert_called_once_with(1)

if __name__ == "__main__":
    unittest.main()