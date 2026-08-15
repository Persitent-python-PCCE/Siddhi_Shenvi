import unittest
from unittest.mock import Mock
from model.product import Product
from model.user import User
from service.product_service import ProductService

class TestProductManagement(unittest.TestCase):

    def setUp(self):
        self.product_service = ProductService()
        self.product_service.product_dao = Mock()
        self.product_service.product_dao.category_exists.return_value = True
        
        self.admin = User(1, "Admin", "admin@gmail.com", "admin123", "admin")
        self.customer = User(2, "Siddhi", "siddhi@gmail.com", "123456", "customer")

    def test_valid_product(self):
        product = Product(None, "Laptop", 50000, 10, 1)
        self.product_service.add_product(product, self.admin)
        self.product_service.product_dao.add_product.assert_called_once_with(product)

    def test_negative_stock(self):
        product = Product(None, "Laptop", 50000, -5, 1)
        with self.assertRaises(ValueError):
            self.product_service.add_product(product, self.admin)

    def test_zero_stock(self):
        product = Product(None, "Laptop", 50000, 0, 1)
        self.product_service.add_product(product, self.admin)
        self.product_service.product_dao.add_product.assert_called_once_with(product)

    def test_customer_cannot_add_product(self):
        product = Product(None, "Laptop", 50000, 10, 1)
        with self.assertRaises(PermissionError):
            self.product_service.add_product(product, self.customer)
        self.product_service.product_dao.add_product.assert_not_called()

    def test_get_all_products(self):
        expected_products = [(1, "Laptop", 50000.00, 10, "Electronics")]
        self.product_service.product_dao.get_all_products.return_value = expected_products
        result = self.product_service.get_all_products()
        self.assertEqual(result, expected_products)

    def test_valid_update(self):
        product = Product(1, "Updated Laptop", 55000, 15, 1)
        self.product_service.product_dao.update_product.return_value = 1
        result = self.product_service.update_product(product, self.admin)
        self.assertTrue(result)
        self.product_service.product_dao.update_product.assert_called_once_with(product)

    def test_update_negative_stock(self):
        product = Product(1, "Laptop", 50000, -5, 1)
        with self.assertRaises(ValueError):
            self.product_service.update_product(product, self.admin)

    def test_valid_delete(self):
        self.product_service.product_dao.delete_product.return_value = 1
        result = self.product_service.delete_product(1, self.admin)
        self.assertTrue(result)
        self.product_service.product_dao.delete_product.assert_called_once_with(1)

    def test_customer_cannot_delete_product(self):
        with self.assertRaises(PermissionError):
            self.product_service.delete_product(1, self.customer)
        self.product_service.product_dao.delete_product.assert_not_called()

if __name__ == "__main__":
    unittest.main()