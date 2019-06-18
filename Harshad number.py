def isharshad(num):
    sum = 0
    for x in num :
        sum = sum + int(x)
    if int(num) % sum == 0 :
        return True
    else :
        return False

num = input('Enter the number: ')
print(isharshad(num))