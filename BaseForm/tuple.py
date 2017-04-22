# -*- coding: UTF-8 -*-
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print tuple
print tuple[0]
print tuple[1:2]  # 有逗号，这个数等于废了

print tuple[1:3]

print tuple[2:]
print tinytuple * 2

print tuple + tinytuple

# 和前面的list有一个相同，一个不同
# 1.在求范围的时候都是中括号
# 2. when in list, there is no ",", however in tuple, there is a ugly ','

print "********************************************"
apple = ('runoob', 786, 2.23, 'john', 70.2)
banana = ['runoob', 786, 2.23, 'john', 70.2]

# TypeError: 'tuple' object does not support item assignment
# apple[2] = 1000

banana[2] = 1000
print banana

