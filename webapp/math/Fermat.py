def fermat(n: int, a: int):
    """

    :param n: Entier
    :param a: Entier
    :return: Retourne faux si a^(n-1) % n est différent de 1
    """
    if 2 <= a <= n - 1:
        return (a ** (n - 1) - 1) % n == 0
    else:
        return False