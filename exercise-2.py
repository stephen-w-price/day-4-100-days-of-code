import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random_index = random.randint(0, len(names))
print(random_index)
print(names[random_index])
