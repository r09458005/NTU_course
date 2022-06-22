#請宣告一個整數陣列，內容有5格
#輸入這5格陣列的內容後
#依序印出陣列內容(整數數字)後空一tab(\t)印出該數字個數個*號


star='*'
x=[]
while True:
    n=int(input())
    x.append(n)
    if len(x) > 5:
        continue
    elif len(x)== 5:
        break
    
print(int(x[0]),int(x[0])*star,end='\n',sep='\t')
print(int(x[1]),int(x[1])*star,end='\n',sep='\t')
print(int(x[2]),int(x[2])*star,end='\n',sep='\t')
print(int(x[3]),int(x[3])*star,end='\n',sep='\t')   
print(int(x[4]),int(x[4])*star,end='\n',sep='\t')


