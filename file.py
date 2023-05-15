import random


with open ('file.txt', 'w') as f:
    str_ = [f'{random.randint(0,10)}\n' for elem in range(10)]

    f.writelines (str_  )


