from src.polynomial import add_polynomials


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