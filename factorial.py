def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    print(fact)

n = int(input('Enter the number: ')) 
factorial(n)