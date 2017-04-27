# -*- coding: UTF-8 -*-

Money = 2000


def add_money():
    global Money
    Money += 1


print Money
print "*******************"
add_money()  # only a calculate
print "*******************"
print Money

"""
理解：
    1、局部变量是局部变量，全局变量是全局变量，它们两个没有任何实质性的关系; 虽然名字是相同的;
    2、如果非要让它们有关系的话，那么加上一个:global就可以了
"""

"""
    这里面有几个规律，要记一下：
    1. 函数名称要用小写的，每个单词中间用_连接
    2. 在定义函数的时候，上面是两行空格，这些小的细节也一定要把握好
"""