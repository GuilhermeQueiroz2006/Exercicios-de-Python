times = (
    'Flamengo', 'Palmeiras', 'Cruzeiro', 'Fluminense',
    'Athletico-PR', 'Bahia', 'Atlético-MG', 'Bragantino',
    'Santos', 'Vasco', 'São Paulo', 'Coritiba',
    'Vitória', 'Botafogo','Corinthians', 'Grêmio', 'Mirassol',
    'Internacional', 'Remo', 'Chapecoense'
)

print('-=' * 35)
print(f'Lista dos times do brasileirão {times}', end='\n')
print('-=' * 35)
print(f'Os 5 primeiros times são {times[:5]}')
print('-=' * 35)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 35)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 35)
print(f'O Chapecoense está na {times.index('Chapecoense')+1}° posição')
