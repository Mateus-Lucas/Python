print('\033[1;33m' + '=' * 20 + ' | Desafio 105 | ' + '=' * 20 + '\033[m')

''' Faça um programa que tenha função notas() que pode receber
várias notas de alunos e vai retornar um diocionário com as
seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação(opcional)
- Adicione também as docstrings'''

def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """

    resultado = {
        'total': len(notas),
        'maior': max(notas) if notas else 0,
        'menor': min(notas) if notas else 0,
        'media': sum(notas) / len(notas) if notas else 0
    }

    if sit:
        if resultado['media'] >= 7:
            resultado['situacao'] = 'BOA'
        elif resultado['media'] >= 5:
            resultado['situacao'] = 'RAZOÁVEL'
        else:
            resultado['situacao'] = 'RUIM'

    return resultado

# Programa principal
resp = notas(5.5, 9.5, 10, sit=True)
print(resp)
help(notas)