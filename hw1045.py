#使用者可以輸入一字元並讓程式判斷此字元是大寫或是小寫英文字母、數字或是其它標點符號。
#如果使用者輸入的是小寫英文字母的話，就將其轉大寫後輸出為swap to capital letter X.


cha=str(input())

if cha.isupper() == True:
    print(cha,'is a capital letter.')
    
elif cha.islower() == True:
    print(cha,'is a lowercase letter.')
    print('swap to capital letter',cha.upper(),end='.')

elif cha.isdigit() == True:
    print(cha,'is a number.')

else:
    print(cha,'is a punctuation.')
    


