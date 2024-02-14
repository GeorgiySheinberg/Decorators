from task_2 import logger


@logger('custom.log')
def discriminant(a, b, c):
    """
    Функция для нахождения дискриминанта
    """
    # Ваш алгоритм
    d = b ** 2 - 4 * a * c
    return d


@logger('custom.log')
def solution(a, b, c):
    """
    Функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    if d < 0:
        print('корней нет')
    else:
        x1 = (- b + d ** 0.5) / (2 * a)
        x2 = (- b - d ** 0.5) / (2 * a)
        if x1 != x2:
            print(x1, x2)
        else:
            print(x1)


if __name__ == '__main__':
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)