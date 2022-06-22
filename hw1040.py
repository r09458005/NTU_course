y=[]
while True:
    n=input()
    if n == '-1':
        break
    elif n != '-1':
        y.append(n.upper())
        continue

for ele in y:
    print(ele)
