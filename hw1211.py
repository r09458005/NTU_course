"""
用鍵盤輸入二個整數，並將其放入一list之中
使用參考寫一個 swap(list) 函式，將此list做為引數傳入此swap函式中
將內含兩個整數的list的兩個整數互換位置後於主程式中輸出
ex: 傳入[11,55] => 於函式中改變為[55,11]
※ 此函式不需回傳值
"""

def swap(list):
    list[0],list[1]=list[1],list[0]


 
z=[]
x=input()
y=input()
z.append(x)
z.append(y)
swap(z)
print(z[0])
print(z[1])


