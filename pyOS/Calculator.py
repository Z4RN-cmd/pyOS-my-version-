
try:
    while True:
        operator = input("select operator (type help): ")

        if operator == "help":
            print("""
    +  : add
    -  : subtract
    *  : multiply
    /  : divide
    exit : exit
    """)
            continue

        if operator == "exit":
            break

        number1 = float(input("first number: "))


        number2 = float(input("second number: "))

        if operator == "+":
            print(number1 + number2)
        elif operator == "-":
            print(number1 - number2)
        elif operator == "*":
            print(number1 * number2)
        elif operator == "/":
            print(number1 / number2)
        else:
            print("Unkown perator")
except ValueError as E:
    print(f"{E} is not a valid number.")
except:
    print("Unkown error!")