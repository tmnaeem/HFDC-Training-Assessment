# Using NO BUILT IN LIBRARIES, write a program that satisfies the following problem:

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def sum_of_digits_after_factorial(num):
    fact_total = 1
    sod = 0
    for n in range(num, 0, -1):
        fact_total *= n
    for n in str(fact_total):
        sod += int(n)
    return sod


num = int(input("Enter a number:"))
sod = sum_of_digits_after_factorial(num)
print(f'sum of the digits in the number {num}! is {sod}')