a=int(input("enter starting number:"))
b=int(input("enter ending number:"))


for i in range(a,b+1):
    sum=0
    order=len(str(i))
    temp=i
    for j in range(i):
        digit=temp % 10
        sum = sum +(digit**order)
        temp //= 10

    if(i==sum):
        print(i)
    else:
        pass
