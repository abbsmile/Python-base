# -*- coding: UTF-8 -*-

str1 = "this is string example....exam!!!";
str2 = "exam";

# print str1.index(str2);  # 从0开始数的话，刚好到example的时候,是15



# 这个指的是从哪开始的，
# 如果是从15开始，因为有，就可以;
# 如果是从16开始，因为没有，就不可以;
# 同时，
print str1.index(str2, 16);
# print str1.index(str2, 15);