# -*- coding: UTF-8 -*-

a1 = (1, 2, 3, 4, 5, 6)
a2 = [1, 2, 3, 4, 5]
a3 = [2, 1, [3, [4, 5], 6], 7, [8]]
a4 = 5

# b = list(a1)  # 将元组转化为列表，如果是列表的话，还是列表
# print b


b = list(a4) if isinstance(a4, (list, tuple)) else []
print b
"""
可以看见不管是a1还是a2，最终都会变成一个列表。 对后面一句的 if 有了一个清醒的认识。

但是，else呢？
- 我始终认为 a4 的例子很经典
"""