# encoding: UTF-8
import re


# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

match = pattern.search('hello hello world world world!')

if match:
    print "match已经被匹配上了，什么情况"
    print match.group()
else:
    print "这个暂时它还没有被匹配上！"

