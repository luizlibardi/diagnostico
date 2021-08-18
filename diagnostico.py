"""
Diagnóstico proposto na aula de Estrutura de Dados 1 - UCL, pelo professor André Ribeiro no dia 05/08 para saber o nível da turma.
"""

# Entrada de dados pelo Usuário
eleitores_consultados = int(input('Quantos eleitores foram consultados? '))
votos_branco = int(input('Quantos votos foram em branco? '))
indecisos = int(input('Quantos votos foram indecisos? '))

# Classe para a criação dos candidatos
class Candidatos:
    codigo = 1

    def __init__(self, codigo, nome, intencoes):
        """[Construtor de candidatos"""
        self._codigo = codigo
        self._nome = nome
        self._intencoes = intencoes

    def get_codigo(self):
        """Função que retorna o código do candidato"""
        return self._codigo

    def get_nome(self):
        """Função que retorna o nome do candidato"""
        return self._nome

    def get_intencoes(self):
        """Função que retorna a quantidade de intenções de votos do candidato"""
        return self._intencoes

candidatos = []
codigo = None

# Loop para o usuário fazer a criação dos candidatos
while codigo != 0:
    codigo = int(input('\nCódigo do candidato: '))
    if codigo != 0:
        nome = input('Nome do candidato: ')
        intencoes = int(input('Quantidade de intenções de votos: '))
        candidato = Candidatos(codigo, nome, intencoes)
        candidatos.append(candidato)

def total_votos():
    """Função que retorna o total de votos"""
    return eleitores_consultados + votos_branco + indecisos


def percentual_branco():
    """Função que retorna o a porcentagem de votos em branco"""
    return f'{((votos_branco * 100) / total_votos())}% - Votos em Branco'


def percentual_indecisos():
    """Função que retorna o a porcentagem de votos indecisos"""
    return f'{((indecisos * 100) / total_votos())}% - Indecisos\n'

lista_votos = []

# Letra A) Retorno '%Votos - Nome'
for candidato in candidatos:
    percentual_voto = ((candidato.get_intencoes() * 100) / total_votos()) 
    print(f'{percentual_voto}% - {candidato.get_nome()}')
    lista_votos.append(percentual_voto)
    if percentual_voto > 50:
        print(f'O candidato {candidato.get_nome()} possui alta probabilidade de eleição no primeiro turno') # Letra B)
percentual_branco()
percentual_indecisos()

# Letra C)
if max(lista_votos) - min(lista_votos) < 10:
    print('\nFoi verificado um cenário de grande equilíbrio entre as escolhas dos eleitores') 

# Letra D
print(lista_votos)
if lista_votos == sorted(lista_votos):
    print('O registro foi realizado em ordem crescente de número de intenções de votos') 

