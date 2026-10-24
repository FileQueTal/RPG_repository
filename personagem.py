# Adicionar opção de acrescentar Fotografia de personagem
import math
class Persona:
    def __init__(self, nome, raca, classe, nivel, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        self.__nome = nome
        self.__raca = raca
        self.__classe = classe
        self.__nivel = nivel
        self.__forca = forca
        self.__destreza = destreza
        self.__constituicao = constituicao
        self.__inteligencia = inteligencia
        self.__sabedoria = sabedoria
        self.__carisma = carisma
        
        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, nome):
            self.__nome = nome


        @property
        def raca(self):
            return self.__raca

        @raca.setter
        def raca(self, raca):
            self.__raca = raca


        @property
        def classe(self):
            return self.__classe

        @classe.setter
        def classe(self, classe):
            self.__classe = classe


        @property
        def nivel(self):
            return self.__nivel

        @nivel.setter
        def nivel(self, nivel):
            self.__nivel += nivel


        @property
        def forca(self):
            return self.__forca

        @forca.setter
        def forca(self, forca):
            self.__forca += forca


        @property
        def destreza(self):
            return self.__destreza

        @destreza.setter
        def destreza(self, destreza):
            self.__destreza += destreza


        @property
        def constituicao(self):
            return self.__constituicao

        @constituicao.setter
        def constituicao(self, constituicao):
            self.__constituicao += constituicao


        @property
        def inteligencia(self):
            return self.__inteligencia

        @inteligencia.setter
        def inteligencia(self, inteligencia):
            self.__inteligencia += inteligencia


        @property
        def sabedoria(self):
            return self.__sabedoria

        @sabedoria.setter
        def sabedoria(self, sabedoria):
            self.__sabedoria += sabedoria


        @property
        def carisma(self):
            return self.__carisma

        @carisma.setter
        def carisma(self, carisma):
            self.__carisma += carisma

    def exibir_ficha(self):
        print(f"Nome: {self.__nome}")
        print(f"Raça: {self.__raca}")
        print(f"Classe: {self.__classe}")
        print(f"Nível: {self.__nivel}")
        print(f"Força: {self.__forca}")
        print(f"Destreza: {self.__destreza}")
        print(f"Constituição: {self.__constituicao}")
        print(f"Inteligência: {self.__inteligencia}")
        print(f"Sabedoria: {self.__sabedoria}")
        print(f"Carisma: {self.__carisma}")

    def get_prof(self):
        return math.ceil(self.__nivel/4)+1



"""print('''
          FICHA DE PERSONAGEM
----------------------------------------
''')
Name = input('Digite o nome do personagem: ')
Race = input('Digite a raça do personagem: ')
Class = input('Digite a classe do personagem: ')
Nvl = int(input('Digite o nível do personagem: '))
STR = int(input('Digite a força do personagem: '))
DEX = int(input('Digite a destreza do personagem: '))
CON = int(input('Digite a constituição do personagem: '))
INT = int(input('Digite a inteligência do personagem: '))
WIS = int(input('Digite a sabedoria do personagem: '))
CHA = int(input('Digite o carisma do personagem: '))

Character = Persona(Name, Race, Class, Nvl, STR, DEX, CON, INT, WIS, CHA)
print('''

        PERSONAGEM CRIADO COM SUCESSO!
----------------------------------------------
Siga a descrição do seu personagem:


''')"""
Character = Persona(
    "Aph Theryn", "Híbrido", "Feiticeiro", 5,
    10, 14, 12, 16, 13, 18
)
print(Character.exibir_ficha())
print(Character.get_prof())