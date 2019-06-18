from math import *
def calc(D):
    return sqrt((2*C*D)/H)
C = 50
H = 30
D = input().split(',')
D = [str(round(calc(int(i)))) for i in D]
print(",".join(D))
