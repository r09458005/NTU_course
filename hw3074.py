import os
import shutil
name = 'files'
if not os.path.exists(name):
    os.mkdir(name)
else:
    shutil.rmtree('./%s' %name)

number = int(input())
#在files資料夾當中建立f1, f2… fN等N個資料夾
for i in range(number):
    os.makedirs("./%s/f%d" %(name,i+1))

#列出files的資料夾內容
get_list1 = os.listdir(name)
new_list1 = sorted(get_list1)
print(new_list1)

rename = os.rename(os.path.join(name,new_list1[0]),os.path.join(name,'folder1'))
get_list2 = os.listdir(name)
new_list2 = sorted(get_list2)
print(new_list2)
shutil.rmtree('./files/folder1')
get_list3 = os.listdir(name)
new_list3 = sorted(get_list3)
print(new_list3)
shutil.rmtree('./%s' %name)
