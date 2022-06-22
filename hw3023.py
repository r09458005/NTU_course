#讓使用者輸入數字，直到-1結束
#請列出所有數字之後
#再列出由數字小到大排序的串列
#加總內容超過30的數字後輸出

y=[]
sum30=0
while True:
    n=int(input())
    if n == -1:
        break
    elif n != -1:
        y.append(n)
        continue

print(y)

number_list = list(map(int,list(y)))#采用map函数，将字符串列表中的每一个字符转换成数字。在得到数字列表后，采用sort()函数就可以对其进行排序了。
number_list.sort()
print(number_list)

for i in range (len(y)):
    y[i]=int(y[i])
    if y[i]>30:
        sum30 += int(y[i])
print(sum30)
