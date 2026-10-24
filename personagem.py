# Adicionar opção de acrescentar Fotografia de personagem

class Persona:
    def __init__(self, nome, raca, classe, nivel, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.nivel = nivel
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    def exibir_ficha(self):
        print(f"Nome: {self.nome}")
        print(f"Raça: {self.raca}")
        print(f"Classe: {self.classe}")
        print(f"Nível: {self.nivel}")
        print(f"Força: {self.forca}")
        print(f"Destreza: {self.destreza}")
        print(f"Constituição: {self.constituicao}")
        print(f"Inteligência: {self.inteligencia}")
        print(f"Sabedoria: {self.sabedoria}")
        print(f"Carisma: {self.carisma}")


print('''
          FICHA DE PERSONAGEM
----------------------------------------
''')
Name = input('Digite o nome do personagem: ')
Rç = input('Digite a raça do personagem: ')
Class = input('Digite a classe do personagem: ')
Nvl = int(input('Digite o nível do personagem: '))
STR = int(input('Digite a força do personagem: '))
DEX = int(input('Digite a destreza do personagem: '))
CON = int(input('Digite a constituição do personagem: '))
INT = int(input('Digite a inteligência do personagem: '))
WIS = int(input('Digite a sabedoria do personagem: '))
CHA = int(input('Digite o carisma do personagem: '))

Character = Persona(Name, Rç, Class, Nvl, STR, DEX, CON, INT, WIS, CHA)
print('''

        PERSONAGEM CRIADO COM SUCESSO!
----------------------------------------------
Siga a descrição do seu personagem:


''')
print(Character.exibir_ficha())