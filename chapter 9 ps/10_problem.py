# 10. Write a program to wipe out the content of a file using python.

with open("this.txt", "w") as f:
    f.write("")
print("Content of file wiped out successfully")