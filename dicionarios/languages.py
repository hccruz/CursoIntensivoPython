favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for nome, linguagem in favorite_languages.items():
    print(f'A linguagem favorita de {nome.title()} é {linguagem.title()}.')

amigos = ['phil', 'sarah']

for nome in favorite_languages.keys():
    print(nome.title())
    if nome in amigos:
        print(f'Olá {nome.title()}, eu vi que sua linguagem favorita é {favorite_languages[nome].title()}!')

if 'erin' not in favorite_languages.keys():
    print('Erin, por favor faça nossa pesquisa!\n')

for nome in sorted(favorite_languages.keys()):
    print(f'{nome.title()}, obrigado por responder a pesquuisa.')
