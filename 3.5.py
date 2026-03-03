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
    for _ in range(1000):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        assert fast_mul(a, b) == a * b, f"Ошибка: {a} * {b}"
    print("Все тесты пройдены")


test_fast_mul()
