# encoding: UTF-8
import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

match = pattern.match('hello world!')

if match:
    print match

    # 它们俩是一样的
    print match.group()
    print match.group(0)

    # print match.group(1)

"""
group([group1, …]):
获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。
group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；
不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
"""