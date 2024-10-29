from scripts.api_data import api_info
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


