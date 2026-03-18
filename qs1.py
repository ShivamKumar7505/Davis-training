## Question 1: A shopkeeper wants to calculate total bill after discount.
## Input: Enter price and discount percentage
## Output: Final price after discount

## input

price = float(input("Enter the price: "))

discount = float(input("Enter the discount percentage: "))

## formula
final_price = price - (price * discount / 100)

print("Final price after discount is:", final_price)

'''output
Enter the price: 100
Enter the discount percentage: 10
Final price after discount is: 90.0
'''
