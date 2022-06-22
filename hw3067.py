'''
從這兩大堆物品中
在itemsA中新增二樣水果並刪除「蘋果」
在itemsB中新增二樣水果並刪除「蓮霧」
請列出
itemsA的水果
itemsB的水果
所有的水果且不重覆
兩者皆有的水果
itemsA獨有的水果
itemsB獨有的水果
兩者不重覆的水果

最後將結果轉換成為list並排序後輸出

math={'柯南','灰原','步美','美環','光彥'}
english={'柯南','灰原','丸尾','野口','步美'}
print('數學及格且英文不及格的同學名單',math-english)
print('英文及格且數學不及格的同學名單',english-math)
print('兩科皆及格名單',math.intersection(english))
'''
itemA = {"蘋果", "香蕉", "鳳梨", "芭樂"}  # 這是第一個集合
itemB = {"鳳梨", "蘋果", "水梨", "蓮霧"}  # 這是第二個集合

A_1 = input()
A_2 = input()
B_1 = input()
B_2 = input()

itemA.add(A_1)
itemA.add(A_2)
itemA.remove('蘋果')
iA = list(itemA)
print('iA:',sorted(iA))
itemB.add(B_1)
itemB.add(B_2)
itemB.remove('蓮霧')
iB = list(itemB)
print('iB:',sorted(iB))
unionab = itemA.union(itemB)
union = list(unionab)
print('union:',sorted(union))
intersectionab = itemA.intersection(itemB)
intersection = list(intersectionab)
print('intersection:',intersection)
A_diff_B = itemA.difference(itemB)
AdiffB = list(A_diff_B)
print('A diff B:',sorted(AdiffB))
B_diff_A = itemB.difference(itemA)
BdiffA = list(B_diff_A)
print('B diff A:',sorted(BdiffA))
A_xor_B = itemA.symmetric_difference(itemB)
AxorB = list(A_xor_B)
print('A xor B:',sorted(AxorB))


