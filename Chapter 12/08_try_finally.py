def main():
    try:
        a = int(input("Hey,Enter the a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    else:
        print("hey , I am inside of finally ")

main()