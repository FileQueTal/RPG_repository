import random

def rolar_dado(lados, qtd):
    rolagem = []
    for i in range(qtd):
        resultado = random.randint(1, lados)
        rolagem.append('Dado {i}: {resultado}'.format(i=i+1, resultado=resultado))
    return rolagem


print('''
       MENU DE ROLAGEM DE DADOS
----------------------------------------
1 - Dado de 4 lados
2 - Dado de 6 lados
3 - Dado de 8 lados
4 - Dado de 10 lados
5 - Dado de 12 lados
6 - Dado de 20 lados
7 - Dado de 100 lados
----------------------------------------
''')
x = int(input('Escolha o dado que deseja rolar: '))

if x == 1:
    mtt = int(input('Quantos dados serão rolados? '))
    print(rolar_dado(4, mtt))
elif x == 2:
    mtt = int(input('Quantos dados serão rolados? '))
    print(rolar_dado(6, mtt))
elif x == 3:
    mtt = int(input('Quantos dados serão rolados? '))
    print(rolar_dado(8, mtt))
elif x == 4:
    mtt = int(input('Quantos dados serão rolados? '))
    print(rolar_dado(10, mtt))
elif x == 5:
    mtt = int(input('Quantos dados serão rolados? '))
    print(rolar_dado(12, mtt))
elif x == 6:
    mtt = int(input('Quantos dados serão rolados? '))
    print(rolar_dado(20, mtt))
elif x == 7:
    mtt = int(input('Quantos dados serão rolados? '))
    print(rolar_dado(100, mtt))