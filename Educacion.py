import requests
from deep_translator import GoogleTranslator
def numeros(n):
     ">>>>>>>>>>>>>>>>>> EJEMPLO DE USO DE API PARA SOLICITAR DATOS INTERESANTES DE UN NUMERO <<<<<<<<<<<<<<<<<<<"
    url=f"https://numbersapi.p.rapidapi.com/{n}/math"
    querystring={"fragment":"true","json":"´true"}
    headers={'x-rapidapi-key': "KEY",'x-rapidapi-host': "HOST"}
    response=requests.request("GET", url, headers=headers, params=querystring)
     
    respuesta=response.json()
    respuesta=respuesta['text']
    respuesta=GoogleTranslator(source='auto',target="es").translate(text=respuesta)
    return respuesta.capitalize()+"."

def rand(n):
    url=f"https://numbersapi.p.rapidapi.com/{n}/trivia"
    querystring={"fragment":"true","notfound":"floor","json":"true"}
    headers = {'x-rapidapi-key': "KEY",'x-rapidapi-host': "HOST"}

    response=requests.request("GET", url, headers=headers, params=querystring)
    respuesta=response.json()
    respuesta=respuesta['text']
    respuesta=GoogleTranslator(source='auto',target="es").translate(text=respuesta)
    return respuesta.capitalize()+"."
    
