number_input = input("Input number: ")
if int(number_input) > 0:
    converted_to_list = []
    multiply_result = 1
    for numbers_1 in number_input:
        converted_to_list.append(int(numbers_1))
    for numbers_2 in converted_to_list:
        multiply_result = multiply_result * numbers_2
    if multiply_result <= 9:
        print("YES ", multiply_result)
    else:
        print("NO ", multiply_result)

    # Дополнительный цикл для перемножения цифр в результате
    while multiply_result > 9:
        result_digits = [int(digit) for digit in str(multiply_result)]
        multiply_result = 1
        for digit in result_digits:
            multiply_result *= digit

    print("Multiply result of digits: ", multiply_result)

else:
    print("IDI HANYU")
