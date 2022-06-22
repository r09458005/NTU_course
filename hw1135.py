#有一天Alice要寄一個資料給BOB.
#但是她知道網絡上寄文件是很不安全的。
#所以她跟BOB 説好了，BOB要的資料將會是Alice給出去的資料裏的中位數。
#請你找出BOB所要拿到的特殊值。（中位數）。
#Alice 一共會傳給BOB N 個整數， 0 < N < 100000。
#其中每一個整數 A[i], 0< A[i] < 10000。
#請你求出這個數列的中位數。
#Alice 爲了讓BOB方便找到答案，Alice 給出的數字都已經小到大排序完成。
#他們也定了一個秘密，若 N 是雙數的話中位數就取中間兩個數相加后除以二（然後進位）。
 
import math

x=int(input())
y=input().split()

if x % 2 == 1:
        num=int((x)/2)
        print(y[num])
else:
    num1=int((x)/2)
    num2=int((x)/2-1)
    c=(int(y[num1])+int(y[num2]))/2
    print(math.ceil(c))


                
