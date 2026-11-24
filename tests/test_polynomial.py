from src.polynomial import add_polynomials, multiply_polynomials


def test_add_polynomials():
    poly_a = [3, 2, 5]
    poly_b = [1, 4, 2]

    result = add_polynomials(poly_a, poly_b)

    assert result == [4, 6, 7]


def test_add_polynomials_modulo():
    poly_a = [3328, 10]
    poly_b = [5, 20]

    result = add_polynomials(poly_a, poly_b)

    assert result == [4, 30]


def test_different_polynomial_lengths():
    poly_a = [1, 2, 3]
    poly_b = [4, 5]

    try:
        add_polynomials(poly_a, poly_b)
        assert False
    except ValueError:
        assert True
        

from src.polynomial import multiply_polynomials


def test_multiply_polynomials():
    poly_a = [1, 2]
    poly_b = [3, 4]

    result = multiply_polynomials(poly_a, poly_b)

    assert result == [3, 10, 8]


def test_multiply_polynomials_modulo():
    poly_a = [3328, 2]
    poly_b = [2, 3]

    result = multiply_polynomials(poly_a, poly_b)

    assert result == [3327, 1, 6]


def test_multiply_empty_polynomial():
    poly_a = []
    poly_b = [1, 2]

    result = multiply_polynomials(poly_a, poly_b)

    assert result == []