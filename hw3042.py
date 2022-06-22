#abcdefghijklmnopqrstuvwxyz
import string
'''
word_ascii = []
x=[]

while True:
    word = input()
    
    if word == '-1':
        break
    elif word != '-1':
        for i in word: 
            if ord(i)>65:
                ascii_transform = ord(i)-3
                x.append(ascii_transform)
            else:
                ascii_transform = ord(i)
                x.append(ascii_transform)
            word_ascii.append(str(chr(ascii_transform)))
        continue
    
print(word_ascii)
print(''.join(word_ascii))
'''
table = {'a':'x', 'b':'y', 'c':'z', 'd':'a', 'e':'b', 'f':'c', 'g':'d',
         'h':'e', 'i':'f', 'j':'g', 'k':'h', 'l':'i', 'm':'j', 'n':'k',
         'o':'l', 'p':'m', 'q':'n', 'r':'o', 's':'p', 't':'q', 'u':'r',
         'v':'s', 'w':'t', 'x':'u', 'y':'v', 'z':'w'}
#####
all_input = list()
while(1):
    input_str = input()
    if input_str == '-1':
        break
    all_input.append(input_str.lower())
#print(all_input)
######


new_input_list = list()
for word in all_input:
    word1 = ''
    j = 0
    for i in range(len(word)):
        if word[i].isalpha():
            word1 = word1 + table[word[j]]
        else:
            word1 = word1 + word[j] 
        j += 1
    new_input_list.append(word1)


result = ''
for word in new_input_list:
    result = result + word + ' '
print(result[:-1])

    
