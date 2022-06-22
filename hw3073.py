n = int(input())
def return2num(n=0):
    a1 = 1
    a2 = 0
    if n ==0:
        a1 = 1
        a2 = 0
    elif n >0:
        for i in range(n):
            a1 *= (i+1)
            a2 += (i+1)
    return (a1,a2) 
(a1,a2)=return2num(n)
print(a1)
print(a2)
