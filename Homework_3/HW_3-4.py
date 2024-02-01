import random 
random_list = []
random_start = random.randrange(3, 11)
random_end =  random.randrange(3, 11)
if random_start > random_end:
    random_start, random_end = random_end, random_start
for i in range(random_start, random_end):
    random_list.append(i)
print(random_list)