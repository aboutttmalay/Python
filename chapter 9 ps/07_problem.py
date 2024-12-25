# 7. Write a program to find out the line number where python is present from ques 6.


with open("log.txt") as f:
    content = f.readlines()

lineno =1
for line in content:
    if "python" in line.lower():
        print(f"Python is present in line number {lineno}")
        break
    lineno += 1 
else:
    print("Python is not present in the file")    