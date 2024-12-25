f = open("file.txt")

# lines = f.readlines()
# print(lines , type(lines))

# lines1 = f.readlines()
# print(lines1 , type(lines1))

# lines2 = f.readlines()
# print(lines2 , type(lines2))

# lines3 = f.readlines()
# print(lines3 , type(lines3))

# lines4 = f.readlines()
# print(lines4 , type(lines4))

# lines5 = f.readlines()
# print(lines5 == "")

line  = f.readline()
while(line !=""):
    print(line)
    line = f.readline()


f.close()