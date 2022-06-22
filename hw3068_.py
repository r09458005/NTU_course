'''
當使用者分別輸入「P」、「M」或「H」時， 請利用字典(dict)/C++ STL map 的方法
分別輸出「Pikachu」、「Mickey Mouse」或「Mickey Mouse」，請加入以下功能：

可不斷重覆查詢，直到-1結束
如果使用者輸入的是不存在的key會發生錯誤，應如何避免程式錯誤？
如果使用者輸入的是不存在的key，應提示使用者此key不存在，
並令使用者可再輸入一組字串與之前查詢的key組成一對新的可供查詢的資料(pair) 。
'''

key=('P','M','H')
value = ('Pikachu','Mickey Mouse','Hello kitty')
d= dict(zip(key,value))
keyin = 0
while keyin != '-1' :
    keyin = input()

    if keyin in d:
        print(d[keyin])
    elif (keyin not in d) and (keyin != '-1'):
        print('%s does not exist. Enter a new one:' % keyin)
        new_value = input()
        d.update({keyin:new_value})
