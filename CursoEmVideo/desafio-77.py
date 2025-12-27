print('\033[1;33m' + '=' * 20, '| Desafio 77 |', '=' * 20 + '\033[m')

''' Crie um programa que tenha uma tupla con várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais'''

palavras = ('feijao', 'doce', 'carro', 'teclado', 'livro', 'Estojo')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            print(letra, end=' ')
