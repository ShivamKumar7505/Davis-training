# Calculate electricity bill based on units consumed

def calculate_electricity_bill(units):
    if units <= 100:
        bill = units * 0.5
    elif units <= 200:
        bill = (100 * 0.5) + ((units - 100) * 0.75)
    elif units <= 300:
        bill = (100 * 0.5) + (100 * 0.75) + ((units - 200) * 1.20)
    else:
        bill = (100 * 0.5) + (100 * 0.75) + (100 * 1.20) + ((units - 300) * 1.50)
    
    return bill

total_bill = calculate_electricity_bill(350)
print(f"Total electricity bill: {total_bill}")