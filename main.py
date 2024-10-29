from scripts.api_data import api_info, gera_relatorio
import geocoder

g = geocoder.ip('me')
latitude, longitude = g.latlng
cidade, timezone, nascer_sol, por_sol, temperatura, umidade, ultravioleta, nuvens, visibilidade, velocidade_vento, tempo = api_info(latitude, longitude)

print('-' * 30)
print('Bem-vindo(a) ao WeatherInfo')
print('-' * 30)

print(f'Aqui estão as informações do tempo no seu endereço atual: {latitude} - {longitude}\n')

print(f'''
Cidade: {cidade}
Timezone: {timezone}
Nascer do sol: {nascer_sol}
Pôr do sol: {por_sol}
Temperatura: {temperatura}
Umidade: {umidade}
Ultravioleta: {ultravioleta}
Nuvens: {nuvens}
Visibilidade: {visibilidade}
Velocidade do vento: {velocidade_vento}
''')

escolha = str(input('\nDeseja ver um relatorio sobre as condições? (S/N)'))

match escolha.lower():
    case 's':
        print(f'\nRelatório: {gera_relatorio(latitude, longitude)}')
    case 'n':
        print('Tudo bem então, obrigado por nos consultar!')
    case _:
        print('Opção invalida...')
        




