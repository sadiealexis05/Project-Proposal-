import random


def create_shares(value, num_shares, modulus=3329):
    """
    Split a value into random additive shares.

    The shares add up to the original value modulo q.
    """

    shares = []

    if num_shares < 2:
        raise ValueError("At least 2 shares are required.")
    
    
    # Generate random shares except for the last one.
    for i in range(num_shares - 1):
        random_share = random.randrange(modulus)
        shares.append(random_share)

    # Calculate the final share.
    total = sum(shares)
    last_share = (value - total) % modulus

    shares.append(last_share)

    return shares


def reconstruct_secret(shares, modulus=3329):
    """
    Reconstruct the original value from its shares.
    """

    total = sum(shares)

    return total % modulus