import math

while True:
    operator = input("select operator (type help): ")

    if operator == "help":
        print("""
+  : add
-  : subtract
*  : multiply
/  : divide
sqrt : square root
exit : exit
""")
        continue

    if operator == "exit":
        break

    number1 = float(input("first number: "))

    if operator == "sqrt":
        print("Hasil:", math.sqrt(number1))
        continue

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
        print("Operator tidak dikenal")