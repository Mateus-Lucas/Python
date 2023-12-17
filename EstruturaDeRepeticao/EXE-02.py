# 02 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário
# Mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = ''
senha = ''

while True: 
    usuario = input('Informe o usuário: ')
    senha = input('Informe a senha: ')

    if usuario != senha:
        print('Cadastrado com sucesso')
        break
    else:
        print('Usuário não pode ser igual a senha. Tente novamente')