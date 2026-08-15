from dao.product_dao import ProductDAO


class ProductService:

    def __init__(self):
        self.product_dao = ProductDAO()

    def add_product(self, product, user):
        if user.role != "admin":
            raise PermissionError("Only admin can add products.")

        if not product.name.strip():
            raise ValueError("Product name cannot be empty.")

        if product.price <= 0:
            raise ValueError("Price must be greater than zero.")

        if product.stock < 0:
            raise ValueError("Stock cannot be negative.")

        if product.category_id <= 0:
            raise ValueError("Invalid category.")

        product.name = product.name.strip()

        if not self.product_dao.category_exists(product.category_id):
            raise ValueError("Category does not exist.")
        
        return self.product_dao.add_product(product)

    def get_all_products(self):

        return self.product_dao.get_all_products()

    def update_product(self, product, user):
        if user.role != "admin":
            raise PermissionError("Admin can only update products.")

        if product.product_id <= 0:
            raise ValueError("Invalid product ID.")

        if not product.name.strip():
            raise ValueError("Product name cannot be empty.")

        if product.price <= 0:
            raise ValueError("Price must be greater than zero.")

        if product.stock < 0:
            raise ValueError("Stock cannot be negative.")

        if product.category_id <= 0:
            raise ValueError("Invalid category.")

        product.name = product.name.strip()

        if not self.product_dao.category_exists(product.category_id):
            raise ValueError("Category does not exist.")

        rows_updated = self.product_dao.update_product(product)

        if rows_updated == 0:
            raise ValueError("Product not found.")

        return True

    def delete_product(self, product_id, user):
        if user.role != "admin":
            raise PermissionError("Only admin can delete products.")

        if product_id <= 0:
            raise ValueError("Invalid product ID.")

        rows_deleted = self.product_dao.delete_product(product_id)

        if rows_deleted == 0:
            raise ValueError("Product not found.")

        return True

    def get_products_paginated(
        self,
        page=1,
        page_size=10
    ):

        if page <= 0:
            raise ValueError(
                "Page number must be greater than zero."
            )

        if page_size <= 0:
            raise ValueError(
                "Page size must be greater than zero."
            )

        total_products = self.product_dao.get_total_products()

        total_pages = (
            total_products + page_size - 1
        ) // page_size

        if total_pages == 0:
            total_pages = 1

        if page > total_pages:
            raise ValueError(
                "Page does not exist."
            )

        products = self.product_dao.get_products_by_page(
            page,
            page_size
        )

        return products, total_pages


    def get_products_by_category(
            self,
            category_id,
            page=1,
            page_size=10
        ):

            if category_id <= 0:
                raise ValueError(
                    "Invalid category."
                )

            if page <= 0:
                raise ValueError(
                    "Page number must be greater than zero."
                )

            if page_size <= 0:
                raise ValueError(
                    "Page size must be greater than zero."
                )

            if not self.product_dao.category_exists(
                category_id
            ):
                raise ValueError(
                    "Category does not exist."
                )

            total_products = (
                self.product_dao
                .get_total_products_by_category(
                    category_id
                )
            )

            total_pages = (
                total_products + page_size - 1
            ) // page_size

            if total_pages == 0:
                total_pages = 1

            if page > total_pages:
                raise ValueError(
                    "Page does not exist."
                )

            products = (
                self.product_dao.get_products_by_category(
                    category_id,
                    page,
                    page_size
                )
            )

            return products, total_pages

    def get_all_categories(self):

        return self.product_dao.get_all_categories()