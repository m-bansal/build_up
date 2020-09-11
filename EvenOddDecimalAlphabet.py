while True:
    num = input("Enter a number: ")
    try:
        num = int(num)
        if num%2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError:
        try:
            num = float(num)
            print("It is a decimal number")
        except ValueError:
            print("It is not a number.")
