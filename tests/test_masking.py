from src.masking import create_shares, reconstruct_secret


def test_two_shares_reconstruct_secret():
    value = 15

    shares = create_shares(value, 2)

    result = reconstruct_secret(shares)

    assert result == value


def test_three_shares_reconstruct_secret():
    value = 100

    shares = create_shares(value, 3)

    result = reconstruct_secret(shares)

    assert result == value


def test_shares_are_within_modulus():
    shares = create_shares(15, 3)

    for share in shares:
        assert 0 <= share < 3329


def test_negative_value():
    value = -2

    shares = create_shares(value, 2)

    result = reconstruct_secret(shares)

    assert result == 3327
    
def test_invalid_number_of_shares():
    try:
        create_shares(15, 1)
        assert False
    except ValueError:
        assert True