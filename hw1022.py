a = int(input())
for v in range(a):
    for i in range(a-v-1):
         print(' ',end='')
    for j in range(v+1):    
        print('*',end='')
    print('\n',end='')
