library=[]
gotyou=[]
notfound=[]

while True:
    book = input()
    if book == 'q':
        break
    elif book != 'q':
        library.append(book.lower())
        continue

for i in range(1,len(library),1):
    if library[i] == library[0]:
        gotyou.append(library[i])
        x = i
    else:
        notfound.append(library[i])
        
if len(gotyou) != 0:
    print("Yes",x)
    
else:
    print("No",len(library)-1)
