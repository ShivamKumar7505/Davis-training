## Question 6: A shopkeeper wants to calculate total bill after discount.
## Input: Enter price and discount percentage
## Output: Final price after discount
## using function

def total_discount(price, discount):
    return price - (price * discount / 100)

## input

price = float(input("Enter the price: "))
discount = float(input("Enter the discount percentage: "))
print("Final price after discount is:", total_discount(price, discount))

'''output
Enter the price: 100
Enter the discount percentage: 10
Final price after discount is: 90.0
'''

