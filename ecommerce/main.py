from controller.user_controller import UserController
from controller.product_controller import ProductController
from controller.cart_controller import CartController
from controller.order_controller import OrderController

user_controller = UserController()
product_controller = ProductController()
cart_controller = CartController()
order_controller = OrderController()

while True:
    print("\n===== Welcome =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_controller.add_user()

    elif choice == "2":
        user = user_controller.login_user()
        
        if user:
            if user.role == "admin":
                while True:
                    print("\n===== ADMIN MENU =====")
                    print("1. View Products")
                    print("2. Add Product")
                    print("3. Update Product")
                    print("4. Delete Product")
                    print("5. Backup Orders")
                    print("6. Logout")

                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        product_controller.view_products()
                    elif admin_choice == "2":
                        product_controller.add_product(user)
                    elif admin_choice == "3":
                        product_controller.update_product(user)
                    elif admin_choice == "4":
                        product_controller.delete_product(user)
                    elif admin_choice == "5":
                        order_controller.backup_orders()
                    elif admin_choice == "6":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")

            else:
                while True:
                    print("\n===== CUSTOMER MENU =====")
                    print("1. View Products")
                    print("2. Browse Products by Category")
                    print("3. Add to Cart")
                    print("4. Remove from Cart")
                    print("5. View Cart")
                    print("6. Clear Cart")
                    print("7. Place Order")
                    print("8. View Order History")
                    print("9. Logout")

                    customer_choice = input("Enter your choice: ")

                    if customer_choice == "1":
                        product_controller.view_products()
                    elif customer_choice == "2":
                        product_controller.browse_by_category()
                    elif customer_choice == "3":
                        cart_controller.add_to_cart(user)
                    elif customer_choice == "4":
                        cart_controller.remove_from_cart(user)
                    elif customer_choice == "5":
                        cart_controller.view_cart(user)
                    elif customer_choice == "6":
                        cart_controller.clear_cart(user)
                    elif customer_choice == "7":
                        order_controller.place_order(user)
                    elif customer_choice == "8":
                        order_controller.view_order_history(user)
                    elif customer_choice == "9":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")

    elif choice == "3":
        print("Thank you for visiting.")
        break
        
    else:
        print("Invalid choice.")