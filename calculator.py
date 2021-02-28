def sum(x, y):
    """
    Sum x and y

    >>> sum(10, 20)
    30

    >>> sum(10.5, 2.2)
    12.7
    """
    assert isinstance(x, (int, float)), 'X must be int or float'
    assert isinstance(y, (int, float)), 'Y must be int or float'
    return x+y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)