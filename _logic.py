sec=int(input("Enter a second:"))
hours = sec//3600
min = (sec - hours*3600)//60
print(sec, "second is ", hours, "hours and ", min, "minute")