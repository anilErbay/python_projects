# Choosing a random Viking female name for my kitten! =)

import random


def pet_name(file_name):
    with open(file_name) as f:
        f_content_list = f.readlines()
        pet_name = random.choice(f_content_list)
        return pet_name


pet_name = print(pet_name('pet_name.txt'))
