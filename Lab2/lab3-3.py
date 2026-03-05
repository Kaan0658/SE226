n=int(input('Enter a number which is between 3 and 9 inclusive:'))
if n<3 or n>9:
    print('number is not between those two numbers')
else:
    for a in range(n):
        print('*'*a)
    while n>0:
        print('*'*n)
        n=n-1


