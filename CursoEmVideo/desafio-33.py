def main():
    print('=' * 11, '| Desafio 33 |' ,'=' * 11)
    print("\nFaça um programa que  leia três números e mostre qual é o maior e qual é o menor")

    try:
        numeros = [
            int(input("informe o primeiro número: ")),
            int(input("informe o segundo número: ")),
            int(input("informe o terceiro número: "))
        ]
    except ValueError:
        print("⚠️ Entrada inválida. Digite apenas números inteiros.")
        return
    
    maior = max(numeros)
    menor = min(numeros)

    print('-=-' * 20)
    print(f"O maior número é {maior}")
    print(f"O menor número é {menor}")

if __name__=="__main__":
    main()


# print('=' * 11, '| Desafio 33 |' ,'=' * 11)

# '''
#  Faça um programa que  leia três números e mostre qual é o maior e qual é o menor
# '''

# num1 = int(input('Informe o primeiro número: '))
# num2 = int(input('Informe o segundo número: '))
# num3 = int(input('Informe o terceiro número: '))
# print('-=-' * 20)

# if num1 > num2 and num1 > num3:
#     print(f'O maior número é {num1}')
#     if num2 > num3:
#         print(f'O menor número é {num3}')
#     else:
#         print(f'O menor número é {num2}')
# elif num2 > num3:
#     print(f'O maior número é {num2}')
#     if num1 > num3:
#         print(f'O menor número é {num3}')
#     else: 
#         print(f'O menor número é {num1}')
# else:
#     print(f'O maior número é {num3}')
#     if num1 > num2:
#         print(f'O menor número é {num2}')
#     else:
#         print(f'O menor número é {num1}')