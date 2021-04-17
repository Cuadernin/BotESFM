import requests
from deep_translator import GoogleTranslator
def numeros(n):
    url=f"https://numbersapi.p.rapidapi.com/{n}/math"
    querystring={"fragment":"true","json":"´true"}
    headers={
        'x-rapidapi-key': "5c7d84061amshb6ada123e8de3fcp104033jsne3d05d482678",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }
    response=requests.request("GET", url, headers=headers, params=querystring)
    respuesta=response.json()
    respuesta=respuesta['text']
    respuesta=GoogleTranslator(source='auto',target="es").translate(text=respuesta)
    return respuesta.capitalize()+"."

def rand(n):
    url=f"https://numbersapi.p.rapidapi.com/{n}/trivia"
    querystring={"fragment":"true","notfound":"floor","json":"true"}
    headers = {
    'x-rapidapi-key': "5c7d84061amshb6ada123e8de3fcp104033jsne3d05d482678",
    'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }
    response=requests.request("GET", url, headers=headers, params=querystring)
    respuesta=response.json()
    respuesta=respuesta['text']
    respuesta=GoogleTranslator(source='auto',target="es").translate(text=respuesta)
    return respuesta.capitalize()+"."