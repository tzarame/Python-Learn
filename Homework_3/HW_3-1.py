while True: 
    #fix for empty string
    result = "Program terminated"
    #inputs
    number_1 = input("Enter fist number: ")
    number_1 = int(number_1)
    number_2 = input("Enter second number: ")
    number_2 = int(number_2)
    operator = input("Enter math operator, + - * / ")
    if number_1 == "quit":
        break
    elif operator == "+":
        result = number_1 + number_2
        print(number_1, operator, number_2,"=", result)
    elif operator == "-":
        result = number_1 - number_2
        print(number_1, operator, number_2,"=", result)
    elif operator == "*":
        result = number_1 * number_2
        print(number_1, operator, number_2,"=", result)
    elif operator == "/":
        if number_2 == 0:
            result = "Error: divided by zero"
            print(result)
        else:
            result = number_1 / number_2
            print(number_1, operator, number_2,"=", result)