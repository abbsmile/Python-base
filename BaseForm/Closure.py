# def line_conf():
#     def line(x):
#         return 2 * x + 1
#
#     return line  # return a function object
#
# my_line = line_conf()
# print(my_line(6))


def line_conf():
    b = 15

    def line(x):
        return 2 * x + b

    return line  # return a function object


b = 5
my_line = line_conf()
print(my_line(5))

