## Add code below with answer clearly stated
def find_factorial(n, fact):
    if n < 0:
     print("Factorial does not exist for negative numbers")
    elif n == 0:
     print("The factorial of 0 is 1")
    else:
        for i in range(1,n + 1):
            fact = fact*i
    print("The factorial of",num,"is",fact)
    return fact

def sum_digits(output):
    sum=0
    my_list = [int(x) for x in str(output)]
    for i in my_list:
        sum +=i
    return sum

num = int(input("Enter a number: "))
factorial = 1

factorial_result = find_factorial(num,factorial)
sum_result       = sum_digits(factorial_result)
print("Sum of number is :", sum_result)
