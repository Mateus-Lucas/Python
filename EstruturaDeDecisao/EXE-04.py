# 04 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')
vogais = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

if letra in vogais:
    print(f'A letra {letra} é uma vogal')
else: 
    print(f'A letra {letra} é uma consoante')