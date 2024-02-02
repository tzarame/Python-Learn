input_list = [1, 4, 3, 5, 3, 6, 7]
list_1 = []
list_2 = []
if input_list == []:
    print(list_1)
    print(list_2)
else:
    list_length = len(input_list)
    if list_length % 2 != 0:
        list_half = (list_length // 2) + 1
    else: 
        list_half = (list_length // 2) 
    list_1 = input_list[0:list_half]
    list_2 = input_list[list_half:]
    print(list_1)
    print(list_2)