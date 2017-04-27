# -*- coding:UTF-8 -*-
import support


content = dir(support)
print content


"""
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'print_func', 'print_func2']

特殊字符串变量'__name__'指向模块的名字，__file__指向该模块的导入文件名
"""