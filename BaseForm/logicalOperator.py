# -*- coding: UTF-8 -*-

a = 10
b = 20

if ( a and b ):
   print "1"
else:
   print "0"

if ( a or b ):
   print "1"
else:
   print "0"


# 修改变量 a 的值
a = 0
if ( a and b ):
   print "3 - 变量 a 和 b 都为 true"
else:
   print "3 - 变量 a 和 b 有一个不为 true"

if ( a or b ):
   print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
   print "4 - 变量 a 和 b 都不为 true"

if not( a and b ):
   print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
   print "5 - 变量 a 和 b 都为 true"


# 和其它语言不同的是，它有下面三个不同的东西
#  and， or， not(a and b)