key=('T','H','B')
value = ('Top','Hoodie','Backpack')
d= dict(zip(key,value))
keyin = 0
def get_key(val, my_dict): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 

while keyin != '-1' :
    keyin = input()

    if keyin in d:
        print(d[keyin])
    elif keyin == '-2':
        a=list(sorted(d.keys()))
        b=list()
        for key in a:
            value = d[key]
            b.append(value)
        print('keys:', a)
        print('values:', b)
    elif keyin == '-3':
        del_key = input()
        if del_key in d:
            del d[del_key]
        else:
            print('key %s does not exist, cannot delete.' % del_key)
    elif (keyin not in d) and (keyin != '-1'):
        print('%s does not exist. Enter a new product category:' % keyin)
        new_value = input()
        d.update({keyin:new_value})
