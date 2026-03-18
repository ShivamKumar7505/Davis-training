#  Create a function to calculate simple interest.

def simple_interest(principle , rate , time):
    interest = (principle * rate * time) / 100
    return interest

principle = float(input("Enter the principle: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))

interest = simple_interest(principle , rate , time)
print("The simple interest is: ", interest)
