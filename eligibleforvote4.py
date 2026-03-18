##Question 17: Check whether a person is eligible to vote.
##Input: Enter age
##Output: Eligible / Not Eligible


# Enter the age
age = int(input("Enter age: "))

while True:
    if age >= 18:
        print("Eligible")
        break
    print("Not Eligible")
    break
