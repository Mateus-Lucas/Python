# ============================================
# 🎓 AULA: FUNÇÕES EM PYTHON (VERSÃO DIDÁTICA)
# Autor: Mateus Lucas + Curso em Vídeo (adaptado)
# ============================================

# 🎨 CORES ANSI
RESET = '\033[m'
AMARELO = '\033[1;33m'
AZUL = '\033[1;34m'
VERDE = '\033[1;32m'
CIANO = '\033[1;36m'
MAGENTA = '\033[1;35m'
VERMELHO = '\033[1;31m'

# ============================================
# 🔹 FUNÇÃO 1 — SOMA COM PARÂMETROS
# ============================================

def soma(a, b):
    """Recebe dois números e mostra a soma."""
    print(CIANO + '-' * 40)
    print(f'Valores recebidos → A = {a} | B = {b}')
    resultado = a + b
    print(VERDE + f'Soma = {resultado}')
    print(CIANO + '-' * 40 + RESET)


print(AMARELO + '\nFUNÇÃO 1 — SOMA' + RESET)
soma(4, 5)
soma(8, 9)
soma(2, 1)

print(MAGENTA + 'Ordem nomeada dos parâmetros:' + RESET)
soma(b=3, a=4)

# ============================================
# 🔹 FUNÇÃO 2 — TÍTULO FORMATADO
# ============================================

def titulo(texto):
    """Exibe um título centralizado."""
    print(AZUL + '=' * 50)
    print(texto.center(50))
    print('=' * 50 + RESET)


print(AMARELO + '\nFUNÇÃO 2 — TÍTULOS' + RESET)
titulo('CURSO EM VÍDEO')
titulo('APRENDA PYTHON')
titulo('MATEUS LUCAS')

# ============================================
# 🔹 FUNÇÃO 3 — PARÂMETROS VARIÁVEIS (*args)
# ============================================

def contador(*numeros):
    """Mostra valores recebidos e quantidade."""
    print(MAGENTA + '-' * 50)
    print('Valores recebidos:', end=' ')
    
    for n in numeros:
        print(n, end=' ')
    
    print('FIM!')
    print(VERDE + f'Total de números: {len(numeros)}')
    print(MAGENTA + '-' * 50 + RESET)


print(AMARELO + '\nFUNÇÃO 3 — *args (QUANTIDADE VARIÁVEL)' + RESET)
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# ============================================
# 🔹 FUNÇÃO 4 — MODIFICANDO LISTA (REFERÊNCIA)
# ============================================

def dobra(lista):
    """Dobra os valores de uma lista (altera original)."""
    print(CIANO + '→ Dobrar valores da lista...' + RESET)
    for i in range(len(lista)):
        lista[i] *= 2


print(AMARELO + '\nFUNÇÃO 4 — LISTAS (POR REFERÊNCIA)' + RESET)

valores = [6, 3, 9, 1, 0, 2]

print('Lista original:', AZUL + str(valores) + RESET)

dobra(valores)

print('Lista dobrada :', VERDE + str(valores) + RESET)

# ============================================
# ✅ FIM DA AULA
# ============================================

print(AMARELO + '\n✔ Aula concluída — Funções em Python' + RESET)