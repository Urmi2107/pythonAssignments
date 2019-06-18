def squares(n):
    square = dict()
    for i in range (1,n+1):
        square[i] = i * i
    print(square)
 
n = int(input("Enter the number:"))
squares(n)