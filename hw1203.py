#有一天，王老先生在整理雜物時無意間發現了以前他年少時的信件。
#那時網絡通訊還不怎麽發達所以王先生就是靠寫信來聯係朋友（把妹）。
#翻到了一封與初戀女友的信，
#其中一封有著許多問題和大大小小的 yes 和 no.
#深藏心底的回憶如潮水般湧來回憶起，
#這是他跟初戀女友之間的小秘密。
#因爲當年的信件隱私安全不是很完善，他們之間的問題于回答容易被別人看到。
#所以他們私下定了一個規矩。
#如果回答是全部大寫的 YES 或是NO 那麽表示是反對的。
#反之如果是全部小寫的 yes 或是no 表示是贊成的。
#如果是大小寫混雜的 yEs 或是 nO 或是 yeS 等等皆爲不確定的。
#王老先生眼花很難辨認到底yes YeS YES 等等的差別，
#所以請你來幫他統計一下那些回答中表示贊成、反對和不確定的分別有幾個。

num=int(input())
sec=[]
noo=[]
yess=[]
unknown=[]

while True:
    y=input()
    sec.append(y)
    if len(sec) != num:
        if y == 'YES' or y == 'NO':
            noo.append(y)
        elif y == 'yes' or y =='no':
            yess.append(y)
        elif y =='Yes' or y=='yEs' or y=='yeS' or y=='YEs' or y=='YeS' or y=='yeS' or y =='No' or y =='nO':
            unknown.append(y)
        continue

    elif len(sec) == num:
        if y == 'YES' or y == 'NO':
            noo.append(y)
        elif y == 'yes' or y =='no':
            yess.append(y)
        elif y =='Yes' or y=='yEs' or y=='yeS' or y=='YEs' or y=='YeS' or y=='yeS' or y =='No' or y =='nO':
            unknown.append(y)
        break
        


print(len(yess),len(noo),len(unknown))
    

            
