from main import quadratic_equation
import pytest


def test_positive_discriminant():
    assert quadratic_equation(a=1, b=-5, c=6) == [2.0, 3.0]


def test_zero_discriminant():
    assert quadratic_equation(a=1, b=-2, c=1) == [1.0]


def test_negative_discriminant():
    assert quadratic_equation(a=3, b=-1, c=7) == "Действительных корней нет."


def test_wrong_type_parameters():
    assert quadratic_equation(a="string", b=3, c=-4) == "Неверный тип коэффициентов, необходимы действительные числа."
    assert quadratic_equation(a=1, b=[3], c=-4) == "Неверный тип коэффициентов, необходимы действительные числа."
    assert quadratic_equation(a=4, b=3, c="string") == "Неверный тип коэффициентов, необходимы действительные числа."


def test_a_equals_zero():
    assert quadratic_equation(a=0, b=2, c=-4) == "Это не квадратное уравнение."


def test_b_equals_zero_c_greater_zero():
    assert quadratic_equation(a=2, b=0, c=16) == "Уравнение имеет комплексные корни."


# def test_less_number_of_parameters():
#     with pytest.raises(TypeError):
#         quadratic_equation(b=1, c=3)
#
#
# def test_more_number_of_parameters():
#     with pytest.raises(TypeError):
#         quadratic_equation(a=4, b=-1, c=3, d=14)


if __name__ == '__main__':
    pytest.main()
