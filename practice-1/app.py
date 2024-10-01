import string
import itertools

password = "12312123"
nums = string.digits
count = 0
lengh = 0
flag = False


def combinations(chars, length):
    yield from itertools.product(chars, repeat=length)


while True:
    for nums in combinations(nums, 8):
        count += 1
        res = "".join(nums)
        if res == password:
            print(f"Пароль найден. Попыток = {count}, пароль = {res}")
            flag = True
        if flag:
            break
