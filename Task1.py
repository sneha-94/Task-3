
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact 
num = int(input("Enter a number: "))
if num < 0:
    print("Negative number")
else:

    result = factorial(num)

    print("Factorial of", num, "is", result)

    