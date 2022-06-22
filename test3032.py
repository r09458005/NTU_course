intList, floatList = [], []
intResult, floatResult = 1, 1
 
x = ""
 
while True:
    x = input()
 
    if x != "q":
    #輸入數字
 
    #分類
        if x.replace('-','').isdigit() == False:
            floatList.append(float(x))
 
        elif x.replace('-','').isdigit() == True:
            intList.append(int(x))
 
 
    elif x == 'q':
        break
    else:
            print("Please Enter Numbers Only")
            
print(x)
