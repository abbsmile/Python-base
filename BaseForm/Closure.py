# -*- coding: UTF-8 -*-


# def line_conf():
#     def line(x):
#         return 2 * x + 1
#
#     return line  # return a function object
#
# my_line = line_conf()
# print(my_line(6))


# def line_conf():
#     b = 15
#
#     def line(x):
#         return 2 * x + b
#
#     return line  # return a function object
#
#
# b = 5
# my_line = line_conf()
# print(my_line(5))

#
# def funX(x):
#     def funY(y):
#         return x*y
#     return funY
#
# i = funX(5)
# print type(i)
# print i(6)
#
# # or
#
# print funX(8)(6)


# 等于一个是局部变量，一个是全局变量，两个不一样！等于很有毛病的一个东西
# def fun1():
#     x = 5
#     def fun2():
# 我的理解是：这个x,不是上面的x,它们两个不一样。
#         x *= x
#         return x
#     return fun2()
#
# print fun1()



# def Fun1():
#     """
#     但是数组是可以的，现在问题就来了：
#
#     为什么数组是可以的？？？他的解释是：数组不是堆栈
#     :return:
#     """
#     x = [5]
#     def Fun2():
#         # 指针所指向的肯定是一样的，这样就对了！
#         x[0] *= x[0]
#         return x[0]
#     return Fun2()
#
# print Fun1()


