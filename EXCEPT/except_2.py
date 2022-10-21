import random

def gen_password():
    file = open('base_words.txt', encoding='utf-8')
    lst = file.read().splitlines()
    num1 = random.randint(0, 24)
    num2 = random.randint(0, 24)
    paswd1 = lst[num1]
    paswd2 = lst[num2]
    paswd = paswd1+paswd2
    ln_paswd = len(paswd)
    if 8 <= ln_paswd <= 10:
        return paswd
    while True:
        num1 = random.randint(0, 24)
        num2 = random.randint(0, 24)
        paswd1 = lst[num1]
        paswd2 = lst[num2]
        paswd = paswd1 + paswd2
        ln_paswd = len(paswd)
        if 8 <= ln_paswd <= 10:
            file.close()
            return paswd


if __name__ == '__main__':
    print(gen_password())