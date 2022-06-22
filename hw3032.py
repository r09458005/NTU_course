target = list()
while True:
    num = input()
    try:
        val = int(num)
        target.append(val)
        sorted_list = sorted(target)
    except ValueError:
        if num == 'q':
            break
        else:
            print("Please Enter Numbers Only")
            
print(target)
print(sorted_list)
sorted_list.sort(reverse=True)
print(sorted_list)
print(target)
