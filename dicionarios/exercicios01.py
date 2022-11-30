pessoa = {
    'nome': 'Heraldo',
    'sobrenome': 'Cruz',
    'Idade': 50,
    'Cidade': 'Santo André'
}

print(f'Meu nome é {pessoa["nome"]} {pessoa["sobrenome"]} e tenho {pessoa["Idade"]} anos ' +
    f'e moro na cidade de {pessoa["Cidade"]}.')

numero_favoritos = {
    'Heraldo': 7,
    'Renata': 13,
    'Giovane': 9,
    'Lucilia': 12,
    'Pedro': 5
}

print(f'O número favorito do Heraldo é {numero_favoritos["Heraldo"]}, o número favorito da Renata é ' +
f'{numero_favoritos["Renata"]}, o número favorito do Giovane é {numero_favoritos["Giovane"]}, o número favorito da Lucília é ' +
f'{numero_favoritos["Lucilia"]} e o número favorito do Pedro é {numero_favoritos["Pedro"]}.')
