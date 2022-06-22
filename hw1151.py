x='\n'
y=list()
while True:
     n=int(input())
     if n == -1:
         break
     elif n != -1:
         y.append(n)
         t=y[::-1]
         continue

for i in range (len(t)):
     y[i]=str(t[i])
     z=int(y[i])
     print(z,z*x,end='\n',sep='') #輸出倒序整數，並印出該整數個空行
print('--------------------',end='\n',sep='') #題目說要這樣結束#有\n跟沒有\n都判定我error
