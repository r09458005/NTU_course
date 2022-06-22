#請讓使用者依序輸入數字(float或int)，直到輸入q停止。
#列印數字的小數部分的加總值

#但使用者通常都是很暴力的，都不管使用規定，硬是輸入非數字的符號，例如：abc、@#$!%^&...等等的其他符號。
#所以如果輸入非數字的符號，請讓程式就算使用者輸入其他符號也不會出錯

import math
target = list()
while True:
    num = input()

    if num.isalpha() == True:
        if num != 'q':
            continue
        elif num == 'q':
            break

    
    elif num.isalpha() == False:
        x=math.floor(eval(num))
        y=eval(num)-int(x)
        target.append(y)

        
print('%.2f'%sum(target))
        

        
            
    
