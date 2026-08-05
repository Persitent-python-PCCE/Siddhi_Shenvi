def inventory_report(inventory, gst=0.05, **filters):
    categories = sorted({item[1] for item in inventory})
    print(f"Categories: {categories}")

    low_stock = [item[0] for item in filter(lambda x: x[2] < 10, inventory)]
    print(f"[!] Reorder soon (stock < 10): {low_stock}")
    
    prices = dict(map(lambda x: (x[0], x[3] * (1 + gst)), inventory))
    print(f"Prices incl. GST: {prices}")
    
    matches = []
    for name, category, stock, price in inventory:
        is_match = True
        if "category" in filters and category != filters["category"]:
            is_match = False
        if "max_price" in filters and price > filters["max_price"]:
            is_match = False
            
        if is_match:
            matches.append(name)
            
    print(f"Matching filters {filters}: {matches}")
    return matches

inv = [ ("Masala Chai", "Tea", 5, 20), ("Green Tea", "Tea", 15, 30), ("Samosa", "Snack", 8, 15), ("Biscuit", "Snack", 25, 10), ] 
inventory_report(inv, category="Snack", max_price=15)