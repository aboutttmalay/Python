# 6. Write a program to mine a log file and find out whether it contains ‘python’.


with open("log.txt") as f:
    content = f.read()

if "python" in content.lower():
    print("Yes, the file contains 'python'")
else:
    print("No, the file does not contain 'python'")
    