eleitores_consultados = int(input('Quantos eleitores foram consultados? '))
votos_branco = int(input('Quantos votos foram em branco? '))
indecisos = int(input('Quantos votos foram indecisos? '))

class Candidatos:

    def _init_(self, codigo, nome, intencoes):
        self.codigo = codigo
        self.nome = nome
        self.intencoes = intencoes

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
percentual_branco = ((votos_branco * 100) / total_votos)
percentual_indecisos = ((indecisos * 100) / total_votos)
percentual_voto = ((candidato.intencoes * 100) / total_votos)

for candidato in candidatos:
    print(f'{percentual_voto}% - {candidato.nome}')
    print(f'{percentual_branco}% - Votos em Branco')
    print(f'{percentual_indecisos}% - Indecisos\n')
    if percentual_voto > 50:
        print(f'O candidato {candidato.nome} possui alta probabilidade de eleição no primeiro turno')