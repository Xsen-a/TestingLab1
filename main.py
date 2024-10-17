from math import sqrt


def quadratic_equation(a, b, c):
    if type(a) not in [float, int] or type(b) not in [float, int] or type(c) not in [float, int]:
        return "Неверный тип коэффициентов, необходимы действительные числа"
    if a == 0:
        return "Это не квадратное уравнение."
    d = b**2 - 4 * a * c
    if d < 0:
        return "Действительных корней нет."
    if d == 0:
        return [-b / (2 * a)]
    return sorted([(-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)])


def main():
    print(quadratic_equation(1, -3, 2))


if __name__ == '__main__':
    main()
