# Напишіть функцію-генератор prime_generator, яка повертатиме прості числа. 
# Верхня межа цього діапазону визначається параметром цієї функції.

# Наприклад, виклик функції list(prime_generator(10)) повинен відповідати послідовності з чисел [2, 3, 5, 7] . 
# Наступне число в цій послідовності - 11 і воно більше 10 тому воно не потрапляє в цей ряд


def range_generator(limit):
    for i in range(limit + 1):
        yield i

result = range_generator(5)
print(result)