from model.product import Product
from service.product_service import ProductService


class ProductController:

    def __init__(self):
        self.product_service = ProductService()

    def add_product(self):

        name = input("Enter product name: ")

        try:
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            category_id = int(input("Enter category ID: "))

        except ValueError:
            print("Invalid numeric input.")
            return

        product = Product(
            None,
            name,
            price,
            stock,
            category_id
        )

        try:

            product = self.product_service.add_product(product)

            print("\nProduct added successfully!")
            print("Product ID:", product.product_id)

        except (ValueError, PermissionError) as error:

            print("\nProduct could not be added:", error)

    def update_product(self):

        try:

            product_id = int(input("Enter product ID: "))
            name = input("Enter new product name: ")
            price = float(input("Enter new price: "))
            stock = int(input("Enter new stock: "))
            category_id = int(input("Enter new category ID: "))

        except ValueError:

            print("Invalid input.")
            return

        product = Product(
            product_id,
            name,
            price,
            stock,
            category_id
        )

        try:

            self.product_service.update_product(product)

            print("Product updated successfully!")

        except (ValueError, PermissionError) as error:

            print("Update failed:", error)

    def delete_product(self):

        try:
            product_id = int(input("Enter product ID: "))

        except ValueError:
            print("Invalid product ID.")
            return

        try:

            self.product_service.delete_product(product_id)

            print("Product deleted successfully!")

        except (ValueError, PermissionError) as error:

            print("Delete failed:", error)

    def view_products(self):

        page = 1
        page_size = 10

        while True:

            try:

                products, total_pages = (
                    self.product_service
                    .get_products_paginated(
                        page,
                        page_size
                    )
                )

                print("\n===== PRODUCTS =====")

                if not products:
                    print("No products available.")
                    return

                for product in products:

                    print(
                        f"ID: {product[0]} | "
                        f"{product[1]} | "
                        f"₹{product[2]} | "
                        f"Stock: {product[3]} | "
                        f"Category: {product[4]}"
                    )

                print(
                    f"\nPage {page} of {total_pages}"
                )

                print("\nN - Next page")
                print("P - Previous page")
                print("Q - Back")

                choice = input(
                    "Enter choice: "
                ).lower()

                if choice == "n":

                    if page < total_pages:
                        page += 1
                    else:
                        print("Already on last page.")

                elif choice == "p":

                    if page > 1:
                        page -= 1
                    else:
                        print("Already on first page.")

                elif choice == "q":

                    break

                else:

                    print("Invalid choice.")

            except ValueError as error:

                print("Error:", error)

                break

    def browse_by_category(self):

        try:

            categories = (
                self.product_service
                .get_all_categories()
            )

            print("\n===== CATEGORIES =====")

            for category in categories:

                print(
                    f"{category[0]}. {category[1]}"
                )

            category_id = int(
                input(
                    "Enter category ID: "
                )
            )

            page = 1
            page_size = 10

            while True:

                products, total_pages = (
                    self.product_service
                    .get_products_by_category(
                        category_id,
                        page,
                        page_size
                    )
                )

                print(
                    f"\n===== CATEGORY PRODUCTS "
                    f"(Page {page}/{total_pages}) ====="
                )

                for product in products:

                    print(
                        f"ID: {product[0]} | "
                        f"{product[1]} | "
                        f"₹{product[2]} | "
                        f"Stock: {product[3]} | "
                        f"Category: {product[4]}"
                    )

                print("\nN - Next page")
                print("P - Previous page")
                print("Q - Back")

                choice = input(
                    "Enter choice: "
                ).lower()

                if choice == "n":

                    if page < total_pages:
                        page += 1
                    else:
                        print(
                            "Already on last page."
                        )

                elif choice == "p":

                    if page > 1:
                        page -= 1
                    else:
                        print(
                            "Already on first page."
                        )

                elif choice == "q":

                    break

                else:

                    print("Invalid choice.")

        except ValueError as error:

            print("Error:", error)