class EcommerceController:

    def show_user_menu(self, user):

        if user.role == "admin":
            self.show_admin_menu(user)
        else:
            self.show_customer_menu(user)

    def show_admin_menu(self, user):

        print("\n========== ADMIN MENU ==========")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Logout")

    def show_customer_menu(self, user):

        print("\n======== CUSTOMER MENU =========")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Place Order")
        print("6. Order History")
        print("7. Logout")