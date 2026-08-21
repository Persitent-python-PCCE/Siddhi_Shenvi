#Sales
sales = [12, 5, 8, 20, 3, 15, 22]
total_cups = sum(sales)
avg_cups =int(total_cups / len(sales))
def hour(idx):
    h = 8 + idx
    if h < 12:
        return f"{h}AM"        
    elif h == 12:
        return "12PM"         
    else:
        return f"{h - 12}PM"   

rush_hours = [hour(i) for i, cups in enumerate(sales) if cups >= avg_cups]

print(f"Total: {total_cups} cups | Average:int{avg_cups}/hr")
print(f"Rush hours (above average): {', '.join(rush_hours)}")
