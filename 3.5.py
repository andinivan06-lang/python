import random


def fast_mul(x, y):

    res = 0
    while y > 0:
        if y & 1:
            res += x
        x <<= 1
        y >>= 1
    return res


# ТЕСТ


def test_fast_mul():
    k=0
    for _ in range(1000):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        if (fast_mul(a, b) == a * b):
            k+=1

    if k==1000:
         print("все тесты пройдены")
    else:
         print(f"ошибка: {a} * {b}")


test_fast_mul()
