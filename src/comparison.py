def compare_ciphertexts(original, recreated):
    """
    Compare two ciphertexts coefficient by coefficient.

    Return True if they match.
    Return False if they are different.
    """

    # Ciphertexts with different lengths cannot match.
    if len(original) != len(recreated):
        return False

    # Check each coefficient.
    for i in range(len(original)):
        if original[i] != recreated[i]:
            return False

    # Every coefficient matched.
    return True