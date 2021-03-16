def lanche(n):
    assert isinstance(n, int), 'n deve ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Lanche completo!'

    return 'Passar fome!' 