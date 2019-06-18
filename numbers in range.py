def numberRange(begin, end):
    l=[]
    for x in range(begin,end) :
        if x % 7 == 0 and x % 5 != 0 :
            l.append(str(x))
    print(','.join(l))      

numberRange(2000,3200)
