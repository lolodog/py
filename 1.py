""". Найдите натуральные числа промежутка (а,в) такие, чтобы сумма цифр искомого числа и
сумма цифр следующего за ним числа делилась бы на k

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

 Сколько натуральных чисел, не больших заданного числа k, имеют в своем четверичном
представлении ровно три значащих нуля. (можно использовать подпрограммы)

def pr(n):
    su = 0
    while n>0:
        if n%4==0:
            su+=1
        n//=4
    return su
c = 0
k = int(input())
for i in range(k+1):
    if pr(i)==3:
        c+=1

print(c)


На промежутке (m,n) найдите все простые числа. Используйте функцию IsPrime
"""
x,y = map(int,input().split())
for n in range(x,y+1):
        if all(n%i!=0 for i in range(2,n)):
            print(n)


