# Sample code using the walrus operator

# Example 1: Using walrus operator in a while loop
numbers = [1, 2, 3, 4, 5]
i = 0
while (n := len(numbers)) > i:
    print(numbers[i])
    i += 1

# Example 2: Using walrus operator in an if statement
text = "Hello, world!"
if (length := len(text)) > 10:
    print(f"The length of the text is {length}")