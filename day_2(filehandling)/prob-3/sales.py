import csv
import statistics
revenue=[]
category_revenue={}
total = 0
max_revenue=0
top_product=""
revenues=[]

with open("sales.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        quantity=int(row["quantity"])
        price=int(row["unit_price"])
        category=row["category"]
        product=row["product"]
        revenue=quantity*price
        revenues.append(revenue)
        total += revenue
    
        if category not in category_revenue:
            category_revenue[category]=revenue
        else:
            category_revenue[category] += revenue

        
        if(revenue>max_revenue):
            max_revenue=revenue
            top_product=product

    average = statistics.mean(revenues)
        
print("Revenue by Category")
for category, amount in category_revenue.items():
    print(f"{category}: {amount}")

print(f"\nTop Product: {top_product} ({max_revenue})")
print(f"Total Revenue: {total}")
print(f"Avg/Txn: {average}")