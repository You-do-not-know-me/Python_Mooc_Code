# 列表的类型
print(type([1,2]))

a = [1, 2, '3 4', [1, 2]] # 定义一个列表
print(a[0]) # 列表的取值

# 列表的切片操作
print(a[0:2]) 

# 注意切片操作的返回值
print(a[-1:])
print(a[-1])

# 列表的加法，乘法
print(a + [5, 6])
print([1, 2] * 2)
