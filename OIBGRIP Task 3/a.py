a=5
if a > 1:
    for i in range(2, int(a/2)+1 ):
        if ((a % i )== 0):
            
        print(a , "not prime")
        break
    else:
        print (a , "prime")