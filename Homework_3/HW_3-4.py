import random 
random_list = []
random_lenght = random.randrange(3, 11)
for i in range(random_lenght):
    random_list.append(random.randint(0,10))
new_list = [random_list[0], random_list[2], random_list[-2]]
print(new_list)