def cor(texto, codigo):
    return f'\033[{codigo}m{texto}\033[m'


def cor_amarelo(texto):
    return cor(texto, '1;33')


def cor_vermelho(texto):
    return cor(texto, '1;31')


def cor_azul(texto):
    return cor(texto, '1;34')


def cor_verde(texto):
    return cor(texto, '1;32')