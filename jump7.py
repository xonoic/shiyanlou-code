a=1
while a<=100:
    if a%7==0:
        a=a+1
    elif a%10==7:
        a=a+1
    elif a//10==7:
        a=a+1
    else:
        print(a)
        a=a+1

