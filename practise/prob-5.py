order=[("Masala Chai", 3, 20), ("Samosa", 2, 15), ("Green Tea", 1, 30)]

line_totals= list(map(lambda item:round(item[1]*item[2]*1.05,2),order))
grand_total = sum(line_totals)

print(f"Line Totals: {line_totals}")
print(f"Grand Total: Rs.{grand_total:.2f}")

