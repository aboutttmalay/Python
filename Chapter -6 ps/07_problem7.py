# 7. Write a program to find out whether a given post is talking about "Malay" or not.

post  = input("Enter the post : ")

if("Malay".lower() in post.lower()):
    print("This post talking about the malay")
else:
    print("This not talking a malay")