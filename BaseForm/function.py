# -*- coding: UTF-8 -*-


# 可写函数说明
def printinfo(arg1, *vartuple):
    """打印任何传入的参数
    """
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return

# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

"""
这个东西内部是如何调用的还是说不通？并不是怎么想得明白??

前面是参数，后面直接就是那个指针了,那它在里面是如何调用的也是一个问题？？

print var 应该是print一个指针，但是在这里还是说不通？？？？？？
"""
