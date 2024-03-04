""". Найдите натуральные числа промежутка (а,в) такие, чтобы сумма цифр искомого числа и
сумма цифр следующего за ним числа делилась бы на k"""

a = int(input())
b = int(input())
k = int(input())
for x in range(a,b+1):
    u = x
    z = x
    z+=1
    su = 0;su_1 = 0
    while u>0:
        su+=u%10
        u = u//10
    while z>0:
        su_1+=z%10
        z = z//10
    if su%k==0 and su_1%k==0:
        print(x)


