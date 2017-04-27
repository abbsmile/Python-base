
file_open = open("foo.txt", "wb")

print "the file's name is:", file_open.name
print "close or open? :", file_open.closed
print "access_mode:", file_open.mode
print "have to add space in the end:", file_open.softspace  # confusing ?

file_open.closed