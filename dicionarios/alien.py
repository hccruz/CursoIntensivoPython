'''alien_0 = {'color': 'verde', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'Você já ganhou {new_points} pontos!')

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print(f'O alien é {alien_0["color"]}.')

alien_0['color'] = 'amarelo'

print(f'O alien agora é {alien_0["color"]}.')

alien_0['speed'] = 'fast'
print(f'Original x_position: {alien_0["x_position"]}')

# Move o alienígena para a direita
# Determina a distância que o alienígena deve se deslocar de acordo com sua
# velocidade atual

if alien_0['speed'] == 'slow':
    # Este deve ser um alienígena lento
    alien_0['x_position'] += 1
elif alien_0['speed'] == 'medium':
    # Este deve ser um alienígena médio
    alien_0['x_position'] += 2
else:
    # Este deve ser um alienígena rápido
    alien_0['x_position'] += 3

# A nova posição é a posição antiga somada ao incremento
print(f'Nova x_position: {alien_0["x_position"]}')

del alien_0['points']
print(alien_0)

alien_1 = {'color': 'amarelo', 'points': 10}
alien_2 = {'color': 'vermelho', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)'''

# Cria uma lista vazia para armazenar alienígenas
aliens = []

# Cria 20 alienígenas verdes
for alien_number in range(30):
    new_alien = {'color': 'verde', 'points': 5, 'speed': 'lento'}
    aliens.append(new_alien)

for alien in aliens[0:15]:
    if alien['color'] == 'verde':
        alien['color'] = 'amarelo'
        alien['speed'] = 'médio'
        alien['points'] = 10

for alien in aliens[0:5]:
    if alien['color'] == 'amarelo':
        alien['color'] = 'vermelho'
        alien['speed'] = 'rápido'
        alien['points'] = 10

# Mostra os 16 primeiros alienígenas
for alien in aliens[:16]:
    print(alien)

print('...')

# Mostra quantos alienígenas foram criados
print(f'Total de números de alienígenas: {len(aliens)}')
