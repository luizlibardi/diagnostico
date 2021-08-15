eleitores_consultados = int(input('Quantos eleitores foram consultados? '))
votos_branco = int(input('Quantos votos foram em branco? '))
indecisos = int(input('Quantos votos foram indecisos? '))

class Candidatos:
    codigo = 1

    def __init__(self, codigo, nome, intencoes):
        self._codigo = codigo
        self._nome = nome
        self._intencoes = intencoes

    def get_codigo(self):
        return self._codigo
    
    def get_nome(self):
        return self._nome

    def get_intencoes(self):
        return self._intencoes

candidatos = []
codigo = 1
while codigo != 0:
    codigo = int(input('\nCódigo do candidato: '))
    if codigo == 0:
        pass
    else:
        nome = input('Nome do candidato: ')
        intencoes = int(input('Quantidade de intenções de votos: '))
        candidato = Candidatos(codigo, nome, intencoes)
        candidatos.append(candidato)

def total_votos():
    return eleitores_consultados + votos_branco + indecisos

def percentual_branco():
    return f'{((votos_branco * 100) / total_votos())}% - Votos em Branco'

def percentual_indecisos():
    return f'{((indecisos * 100) / total_votos())}% - Indecisos\n'

lista_votos = []

# Letra A)
for candidato in candidatos:
    percentual_voto = ((candidato.get_intencoes() * 100) / total_votos()) 
    print(f'{percentual_voto}% - {candidato.get_nome()}')
    lista_votos.append(percentual_voto)
    if percentual_voto > 50:
        print(f'O candidato {candidato.get_nome()} possui alta probabilidade de eleição no primeiro turno') # Letra B)
percentual_branco()
percentual_indecisos()


if max(lista_votos) - min(lista_votos) < 10:
    print('\nFoi verificado um cenário de grande equilíbrio entre as escolhas dos eleitores') # Letra C)

print(lista_votos)
if sorted(lista_votos) == True:
    print('O registro foi realizado em ordem crescente de número de intenções de votos') # Letra D




