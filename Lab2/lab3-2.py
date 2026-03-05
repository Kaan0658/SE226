n=int(input('Enter a number which is between 10 and 100 inclusive:'))
if n<10 or n>100:
    print('number is not between those two numbers')
else:
    FbCount=0
    FCount=0
    BCount=0
    while n>0:
        if n%7==0:
            n=n-1
            continue
        if n%15==0:
            print("FizzBuzz")
            FbCount=FbCount+1
        elif n%3==0:
            FCount=FCount+1
            print("Fizz")
        elif n%5==0:
            BCount=BCount+1
            print("Buzz")
        else:
            print(n)
        n=n-1
    print("---Summary---")
    print("Fizz count is:",FCount)
    print("Buzz count is:",BCount)
    print("FizzBuzz count is:", FbCount)

