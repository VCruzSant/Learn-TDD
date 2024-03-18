def sum(x, y):
    """Sum X and Y


    Test -> OK
    >>> sum(31, 20)
    51

    Test -> Failure
    >>> sum(30, 20)
    51

    Test -> Failure
    >>> sum('30', 20)

    Test -> OK
    >>> sum('30', 20)
    Traceback (most recent call last):
    ...
    AssertionError: must be int or float
    """
    assert isinstance(x, (int, float)), 'must be int or float'
    assert isinstance(y, (int, float)), 'must be int or float'
    return x + y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
