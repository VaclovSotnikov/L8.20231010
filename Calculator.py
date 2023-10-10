number1 = int(input("enter number 1: "))
number2 = int(input("enter nuber 2: "))
action = input("zenklas matematinio veiksmo: ")

if action == "+":
    print(number1 + number2)
elif action == "-":
    print(number1 - number2)
elif action == "/":
    print(number1 / number2)
elif action == "*":
    print(number1 * number2)
else:
    print("Tokio matematinio veiksmo nezinau")    

