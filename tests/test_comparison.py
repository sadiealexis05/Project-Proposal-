from src.comparison import compare_ciphertexts


def test_matching_ciphertexts():
    original = [10, 20, 30, 40]
    recreated = [10, 20, 30, 40]

    assert compare_ciphertexts(original, recreated) == True


def test_different_ciphertexts():
    original = [10, 20, 30, 40]
    recreated = [10, 20, 31, 40]

    assert compare_ciphertexts(original, recreated) == False


def test_different_lengths():
    original = [10, 20, 30, 40]
    recreated = [10, 20, 30]

    assert compare_ciphertexts(original, recreated) == False


def test_empty_ciphertexts():
    original = []
    recreated = []

    assert compare_ciphertexts(original, recreated) == True