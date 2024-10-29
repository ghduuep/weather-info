import os
from dotenv import load_dotenv
import geocoder
import requests
from datetime import datetime

load_dotenv()

API_KEY = os.getenv('API_KEY')

def formatador(nascer_sol, por_sol, temperatura):
    nascer_sol_convertido = datetime.fromtimestamp(nascer_sol)
    nascer_sol_convertido = nascer_sol_convertido.strftime('%H:%M:%S')

    por_sol_convertido = datetime.fromtimestamp(por_sol)
    por_sol_convertido = por_sol_convertido.strftime('%H:%M:%S')

    temperatura_convertida = temperatura - 273.15

    return nascer_sol_convertido, por_sol_convertido, temperatura_convertida

def api_info(latitude, longitude):
    URL = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={API_KEY}'
    data = requests.get(URL)
    json = data.json()

    g = geocoder.ip('me')

    cidade = g.city
    timezone = json['timezone']
    nascer_sol = json['current']['sunrise']
    por_sol = json['current']['sunset']
    temperatura = json['current']['temp']
    umidade = json['current']['humidity']
    ultravioleta = json['current']['uvi']
    nuvens = json['current']['clouds']
    visibilidade = json['current']['visibility']
    velocidade_vento = json['current']['wind_speed']
    tempo = json['current']['weather'][0]['main']

    nascer_sol_convertido, por_sol_convertido, temperatura_convertida = formatador(nascer_sol, por_sol, temperatura)


    return cidade, timezone, nascer_sol_convertido, por_sol_convertido, temperatura_convertida, umidade, ultravioleta, nuvens, visibilidade, velocidade_vento, tempo




    
