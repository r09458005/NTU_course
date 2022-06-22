import math

input_array = input().split()
n = len(input_array)
median = (sum(input_array[n//2-1:n//2+1])/2.0, lst[n//2])[n % 2] if n else None
ans = math.ceil(median)
print('%.f'%ans)

