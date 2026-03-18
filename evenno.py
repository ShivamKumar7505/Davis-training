## Question 4: Print all even numbers between 1 to N.
## Input: Enter N
## Output: Even numbers list

## input

n = int(input("Enter the number: "))

## formula
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

'''output
Enter the number: 10
2
4
6
8
10
'''
