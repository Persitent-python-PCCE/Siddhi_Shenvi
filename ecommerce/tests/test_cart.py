import unittest
from unittest.mock import Mock
from service.cart_service import CartService

class TestCartManagement(unittest.TestCase):
    def setUp(self):
        self.cart_service = CartService()
        self.cart_service.cart_dao = Mock()
        self.cart_service.product_dao = Mock()

    def test_add_valid_product_to_cart(self):
        self.cart_service.cart_dao.get_cart_by_user.return_value = [(10,)]
        self.cart_service.product_dao.get_product_by_id.return_value = (5, "Laptop", 50000, 10, 1)
        self.cart_service.cart_dao.get_cart_item.return_value = None
        result = self.cart_service.add_to_cart(1, 5, 2)
        self.assertTrue(result)
        self.cart_service.cart_dao.add_cart_item.assert_called_once_with(10, 5, 2)

    def test_insufficient_stock(self):
        self.cart_service.cart_dao.get_cart_by_user.return_value = [(10,)]
        self.cart_service.product_dao.get_product_by_id.return_value = (5, "Laptop", 50000, 5, 1)
        with self.assertRaises(ValueError):
            self.cart_service.add_to_cart(1, 5, 10)
        self.cart_service.cart_dao.add_cart_item.assert_not_called()

    def test_add_existing_product_causes_insufficient_stock(self):
        self.cart_service.cart_dao.get_cart_by_user.return_value = [(10,)]
        self.cart_service.product_dao.get_product_by_id.return_value = (5, "Laptop", 50000, 5, 1)
        self.cart_service.cart_dao.get_cart_item.return_value = (20, 4)
        with self.assertRaises(ValueError):
            self.cart_service.add_to_cart(1, 5, 2)
        self.cart_service.cart_dao.update_cart_item_quantity.assert_not_called()

    def test_view_cart(self):
        self.cart_service.cart_dao.get_cart_by_user.return_value = [(10,)]
        expected_items = [
            (1, 5, "Laptop", 50000, 2, 100000),
            (2, 6, "Mouse", 1200, 1, 1200)
        ]
        self.cart_service.cart_dao.get_cart_items.return_value = expected_items
        result = self.cart_service.view_cart(1)
        self.assertEqual(result, expected_items)

    def test_view_empty_cart(self):
        self.cart_service.cart_dao.get_cart_by_user.return_value = [(10,)]
        self.cart_service.cart_dao.get_cart_items.return_value = []
        result = self.cart_service.view_cart(1)
        self.assertEqual(result, [])

    def test_calculate_cart_total(self):
        self.cart_service.cart_dao.get_cart_by_user.return_value = [(10,)]
        items = [
            (1, 5, "Laptop", 50000, 2, 100000),
            (2, 6, "Mouse", 1200, 1, 1200)
        ]
        self.cart_service.cart_dao.get_cart_items.return_value = items
        result = self.cart_service.calculate_total(1)
        self.assertEqual(result, 101200)

    def test_calculate_total_empty_cart(self):
        self.cart_service.cart_dao.get_cart_by_user.return_value = [(10,)]
        self.cart_service.cart_dao.get_cart_items.return_value = []
        result = self.cart_service.calculate_total(1)
        self.assertEqual(result, 0)

    def test_remove_product_from_cart(self):
        self.cart_service.cart_dao.get_cart_by_user.return_value = [(10,)]
        self.cart_service.cart_dao.remove_cart_item.return_value = 1
        result = self.cart_service.remove_from_cart(1, 5)
        self.assertTrue(result)
        self.cart_service.cart_dao.remove_cart_item.assert_called_once_with(10, 5)

if __name__ == "__main__":
    unittest.main()