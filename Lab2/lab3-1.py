x=int(input('Enter a number which is greater then 1:'))
if x<=1:
    print('number is not greater then 1')
else:
    while x>1:
        if x%2==0:
            x=x/2
            print(x)
        else:
            x=x*3+1
            print(x)




