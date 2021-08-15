eleitores_consultados = int(input('Quantos eleitores foram consultados? '))
votos_branco = int(input('Quantos votos foram em branco? '))
indecisos = int(input('Quantos votos foram indecisos? '))

class Candidatos:
    
    def __init__(self, codigo, nome, intencoes):
        self.codigo = codigo
        self.nome = nome
        self.intencoes = intencoes

    def dict_intencoes(self):
        dict = {'nome': self.nome, 'intencoes': self.intencoes}
        print(dict)
        

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

total_votos = eleitores_consultados + votos_branco + indecisos

def percentual_branco(votos_branco, total_votos):
    percentual_branco = ((votos_branco * 100) / total_votos)
    print(f'{percentual_branco}% - Votos em Branco')

def percentual_indecisos(indecisos, total_votos):
    percentual_indecisos = ((indecisos * 100) / total_votos)
    print(f'{percentual_indecisos}% - Indecisos\n')

for candidato in candidatos:
    percentual_voto = ((candidato.intencoes * 100) / total_votos)
    print(f'{percentual_voto}% - {candidato.nome}')
    
    if percentual_voto > 50:
        print(f'O candidato {candidato.nome} possui alta probabilidade de eleição no primeiro turno')
    #elif max(percentual_voto) : 

# candidato.dict_intencoes()
percentual_branco(votos_branco, total_votos)
percentual_indecisos(indecisos, total_votos)



