# -*- coding: UTF-8 -*-

# -*- coding: UTF-8 -*-

# a = 20
# b = 200

# if ( a is b ):
#    print "1 - a 和 b 有相同的标识"
# else:
#    print "1 - a 和 b 没有相同的标识"


# print id(5)
# print id(6)
#
# print 5 is 5
# print 5 is not 5

# print id(5) is id(5)
# print id(5) is not id(5)

## ？？ id 是一个有待研究的东西？？？？？
a = [1, 2, 3]
b = [1, 2, 3]
print id(a)  # 38967176
print id(b)  # 38991392
# 1. 终于a、b两个值是不一样的了
# 2. 每运行一次，id(a), id(b)的值都会改变，说明
# 解释器在对值很小的int和很短的字符串的时候做了一点小优化，只分配了一个对象，让它们id一样了。

# if ( id(a) is not id(b) ):
#    print "2 - a 和 b 有相同的标识"
# else:
#    print "2 - a 和 b 没有相同的标识"


# # 修改变量 b 的值
# b = 30
# if ( a is b ):
#    print "3 - a 和 b 有相同的标识"
# else:
#    print "3 - a 和 b 没有相同的标识"
#
# if ( a is not b ):
#    print "4 - a 和 b 没有相同的标识"
# else:
#    print "4 - a 和 b 有相同的标识"