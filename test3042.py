word_ascii = []
word = str(input("輸入文字"))
for i in word: 
    ascii_transform = ord(i)+3
    print(chr(ascii_transform))
    word_ascii.append(chr(ascii_transform))
print(word_ascii)
