####Question 11: A shopkeeper wants to calculate total bill after discount.
##Input: Enter price and discount percentage
##Output: Final price after discount 

price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

remaining_percent = 100 - discount
one_percent_value = price / 100
final_price = one_percent_value * remaining_percent

print("Final price after discount:", final_price)

'''output
Enter price: 100
Enter discount percentage: 10
Final price after discount: 90.0
'''












