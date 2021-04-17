import time
import requests
import telebot
import pandas as pd

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from programacion import plataforma
from datos import base,txtprofesores,txtescuela
from Educacion import numeros,rand
from firebase import firebase
from tabulate import tabulate
from ConexionFirebase import conexion,lecturaR,lecturaT
from SugeridosFirebase import sug,lecturaSug,sugerenciasbot
from MaestrosESFM import buscador,consulta
from telebot import types

TOKEN="1617932110:AAH2adUxuwllYrCuI_k6O8sU_KfxhT1R9eI"
bot=telebot.TeleBot(TOKEN)

firebase=firebase.FirebaseApplication("https://base-8fb74-default-rtdb.firebaseio.com/",None)

@bot.message_handler(commands=['start'])
def start(message):
    messages="""Hola😊, espero te encuentres bien. Esta es la versión 1.0 de este bot. Cualquier fallo que encuentres te agradecería muchísimo que nos contactaras. Para conocer lo que puedes hacer por favor escribe /help y lee con atención las intrucciones de uso de cada función🌞. 
    
    ¡ESPERO TE SEA DE UTILIDAD!♥
    """
    chat_id=message.chat.id
    bot.send_message(chat_id=chat_id,text=messages)

# ======================================= AYUDA ======================================= #
@bot.message_handler(commands=['help'])
def help(message): 
    """Crea una funcion cuando escribe HELP"""       #agregar colecciones para cada maestro usando el archivo de excel                
    messages="""A continuacion, la lista de funciones divididas por categorias: 
    
==============================     
========= PROFESORES =========
============================== 
    -- Escribe una reseña de un profesor:
        💬Descripción: Escribe una breve reseña de un profesor (Menos de 250 caracteres).
        🔑Comando: /profesores
       
        Ejemplo: El profesor X es un excelente profesor. Su clase es muy interesante y plantea situaciones del mundo real donde tenemos que hacer uso de las herramientas que nos proporciona en clase.
    
    -- Lee las reseñas que han escrito otros compañeros:
        💬Descripción: Lee las reseñas que han escrito otros alumnos.
        🔑Comando: /lectura 
        
    -- Enlista los profesores disponibles en la base de datos:
        💬Descripción: Lista de profesores.
        🔑Comando: /listas
        
===============================    
========= PROGRAMACIÓN ========
=============================== 
    -- Plataformas para aprender programación:
        💬Descripción: Lista de plataformas donde se puede aprender a programar.
        🔑Comando: /plataformas
    -- Base de datos:
        💬Descripción: Cursos gratuitos de base de datos relacionales.
        🔑Comando: /cursos
        
==============================        
========= SUGERENCIAS ========
==============================  
    -- Sugerencia para mejorar el bot
        💬Descripción: Escribe una sugerencia para el autor de este bot y así seguir mejorándolo.
        🔑Comando: /sugbot
        
==============================        
========== ESCUELA ===========
==============================
    -- Escribir una sugerencia para mejorar la escuela:
        💬Descripción: Escribe una sugerencia o consejo para mejorar algún aspecto de la escuela. 
        🔑Comando: /sugerencia
        
    -- Leer las sugerencias escritas por otros alumnos:
        💬Descripción: Puedes ver las sugerencias escritas por otros alumnos o escribir una. 
        🔑Comando: /leersug    
        
    -- Solicitar constancias:
        💬Descripción: PowerPoint con las instrucciones oficiales para solicitar una constancia. 
        🔑Comando: /constancias  
        
    -- Calendario:
        💬Descripción: Calendario oficial del IPN. 
        🔑Comando: /calendario 
        
    -- Certificados y carta de pasante:
        💬Descripción: Procedimiento para obtener el certificado de estudios y la carta de pasante. 
        🔑Comando: /certificado 
        
==============================        
=========== OTROS ============
==============================
    -- Covid:
        💬Descripción: Confirmados y muertes por estado en México.
        🔑Comando: /covid
        
    -- Datos intersantes acerca de un número:
        💬Descripción: Datos "matemáticos" interesantes acerca de un número ENTERO que escribas (válido desde el 3 al 700).
        🔑Comando: /numero
        
    -- Datos interesantes acerca de un número aleatorio:
        💬Descripción: Datos interesantes sobre un número (válido del 1 al 3500)
        🔑Comando: /random
        
    -- Contacto:
        💬Descripción: Contacto con autor.
        🔑Comando: /contacto
        
    -- ChatBot:
        💬Descripción: Chatea con un chatbot llamado Nuvo. 
        🔑Comando: /nuvo
        📑Nota: Este es el primer chatbot que diseño llamado Nuvo👷.  Por lo que, puede que su respuesta no tenga mucho sentido, estoy trabajando en ello. Para dejar de hablar con él escribe: salir.
    """
    chat_id=message.chat.id
    bot.send_message(chat_id=chat_id,text=messages)
    
# ======================================= PROFESORES  ======================================= # 
#### ESCRITURA DE RESEÑA ####
@bot.message_handler(commands=['profesores'])   
def profesores(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid,text="Escribe el nombre del maestro empezando por el nombre:")
    bot.register_next_step_handler(msg,profesor)

lista=[]
def profesor(message):
    chatid=message.chat.id
    texto=message.text
    maestro=buscador(str(texto))
    lista.append(maestro)
    if maestro==None:
        msg=bot.send_message(chat_id=chatid,text="Lo siento, el profesor no existe en la base de datos. \
            Vuelva a escribir el nombre correctamente.")
        bot.register_next_step_handler(msg, profesor)   
    else:
        msg=bot.reply_to(message, 'Escribe tu reseña:')
        bot.register_next_step_handler(msg, escritura)   

def escritura(message):
    try:
        chatid=message.chat.id
        texto=message.text
        if len(texto)<250:
            username=message.chat.first_name+'_'+message.chat.last_name
            respuesta=conexion(chatid, username,texto,lista[0])
            lista.pop(0)
            if type(respuesta)==dict:
                msg=bot.send_message(chat_id=chatid,text=f'Muchas gracias, {username}.')
            else:
                msg=bot.send_message(chat_id=chatid,text=f'Tal vez el servidor esta dormido.')
        elif len(texto)<16:
            msg=bot.send_message(chat_id=chatid,text='Trata de escribir algo serio. Prueba otra vez.')
            bot.register_next_step_handler(msg, escritura)
        else:  
            #msg=bot.reply_to(message, 'El texto debe contener menos de 250 caracteres. Prueba otra vez')
            msg=bot.send_message(chat_id=chatid,text='El texto debe contener menos de 250 caracteres. Prueba otra vez.')
            bot.register_next_step_handler(msg,escritura)
    except Exception as e:
        bot.send_message(chat_id=message.chat.id,text="Algo raro paso. Lo siento.")
        
        
#### LECTURA DE RESEÑA #### 
@bot.message_handler(commands=['listas'])
def listas(message):
    chatid=message.chat.id
    texto=consulta()
    text=texto[:80]
    txt=tabulate(text,headers=["Id","PROFESOR"])
    bot.send_message(chat_id=chatid,text=txt,parse_mode="Markdown")
    texto2=texto[80:]
    txt2=tabulate(texto2,headers=["Id","PROFESOR"])
    bot.send_message(chat_id=chatid,text=txt2,parse_mode="Markdown")
    

@bot.message_handler(commands=['lectura'])
def lectura(message):
    chatid=message.chat.id
    texto=message.text
    msg=bot.send_message(chat_id=chatid,text="Escribe el nombre del maestro empezando por el nombre:")
    bot.register_next_step_handler(msg,validado)

def validado(message):
    chatid=message.chat.id
    texto=message.text
    maestro=buscador(str(texto))
    if maestro==None:
        msg=bot.send_message(chat_id=chatid,text="Lo siento, el profesor no existe en la base de datos. \
            Vuelva a escribir el nombre correctamente.")
        bot.register_next_step_handler(msg, validado)   
    else:
        txt=txtprofesores(maestro)
        bot.send_document(chat_id=chatid,data=txt,caption='.txt con las consultas.')  

# ======================================= PRINCIPALES  ======================================= #

# ======================================= SUGERENCIAS ======================================= #
@bot.message_handler(commands=['sugbot'])
def sugbot(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid,text="Escribe tu sugerencia:")
    bot.register_next_step_handler(msg,mibot)


def mibot(message):
    try:
        chatid=message.chat.id
        texto=message.text
        if len(texto)<250:
            username=message.chat.first_name+'_'+message.chat.last_name
            respuesta=sugerenciasbot(chatid, username,texto)
            if type(respuesta)==dict:
                msg=bot.send_message(chat_id=chatid,text=f'Muchas gracias, {username}, por tu sugerencia. Esto me ayuda a mejorar el bot.')
            else:
                msg=bot.send_message(chat_id=chatid,text=f'Tal vez el servidor esta dormido.')
        elif len(texto)<16:
            msg=bot.send_message(chat_id=chatid,text='Trata de escribir algo serio. Prueba otra vez.')
            bot.register_next_step_handler(msg, mibot)
        else:  
            msg=bot.send_message(chat_id=chatid,text='El texto debe contener menos de 250 caracteres. Prueba otra vez.')
            bot.register_next_step_handler(msg, mibot)
    except Exception as e:
        bot.send_message(chat_id=message.chat.id,text="Algo raro paso. Lo siento.")
        
# ======================================= ESCUELA  ======================================= #  
@bot.message_handler(commands=['sugerencia'])   
def sugerencia(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid,text="Escribe tu sugerencia:")
    bot.register_next_step_handler(msg,escuela)

def escuela(message):
    try:
        chatid=message.chat.id
        texto=message.text
        if len(texto)<250:
            username=message.chat.first_name+'_'+message.chat.last_name
            respuesta=sug(chatid, username,texto)
            if type(respuesta)==dict:
                msg=bot.send_message(chat_id=chatid,text=f'Muchas gracias, {username}.')
            else:
                msg=bot.send_message(chat_id=chatid,text=f'Tal vez el servidor esta dormido')
        elif len(texto)<16:
            msg=bot.send_message(chat_id=chatid,text='Trata de escribir algo serio. Prueba otra vez.')
            bot.register_next_step_handler(msg, escuela)
        else:  
            #msg=bot.reply_to(message, 'El texto debe contener menos de 250 caracteres. Prueba otra vez')
            msg=bot.send_message(chat_id=chatid,text='El texto debe contener menos de 250 caracteres. Prueba otra vez.')
            bot.register_next_step_handler(msg, escuela)
    except Exception as e:
        bot.send_message(chat_id=message.chat.id,text="Algo raro paso. Lo siento.")

@bot.message_handler(commands=['leersug'])
def leersug(message):
    chatid=message.chat.id
    texto=message.text
    txt=txtescuela()
    bot.send_document(chat_id=chatid,data=txt,caption='txt con las consultas.')  
        
@bot.message_handler(commands=['calendario'])
def calendario(message):
    chatid=message.chat.id
    url='cal-Escolarizada-20-21.pdf'
    with open(url,'rb') as file:
        bot.send_document(chat_id=chatid,data=file,caption='Calendario Oficial del IPN 2020-2021')

@bot.message_handler(commands=['constancias'])
def constancias(message):
    chatid=message.chat.id
    url="PROCED. DE SOLICITUD DE BOLETAS Y CONSTANCIAS año 2021.pdf"
    with open(url,'rb') as file:
        bot.send_document(chat_id=chatid,data=file,caption='Proced. de solicitud de boletas y constancias')

@bot.message_handler(commands=['certificado'])
def certificado(message):
    chatid=message.chat.id
    texto='''Ingresa al siguiente sitio web para seguir el procedimiento: https://www.dae.ipn.mx/certifyCartaDig.aspx.
    No olvides que tardan de 1 a 2 meses en entregarte los documentos.'''
    bot.send_message(chat_id=chatid,text=texto)
    
# ======================================= PROGRAMACION  ======================================= #  
@bot.message_handler(commands=['plataformas'])    
def plataformas(message):
    dato=plataforma()
    chatid=message.chat.id
    bot.send_message(chat_id=chatid,text=dato)   

@bot.message_handler(commands=['cursos'])     
def cursos(message):
    dato=base()
    chatid=message.chat.id
    bot.send_message(chat_id=chatid,text=dato) 
    
# ======================================= OTROS  ======================================= #
@bot.message_handler(commands=['covid']) 
def covid(message):
    link="https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
    querystring={"country":"Mexico"}
    headers={
        'x-rapidapi-key':"5c7d84061amshb6ada123e8de3fcp104033jsne3d05d482678",
        'x-rapidapi-host':"covid-19-coronavirus-statistics.p.rapidapi.com"
        }
    response=requests.request("GET",link,headers=headers, params=querystring)
    data=response.json()
    lista,ciudades,confirmados,muertes=[],[],[],[]
    my_message="""Hola, espero se encuentre bien. A continuación, la informacion diaria de COVID-19 en el pais."""# Customize your message
    for user in data['data']['covid19Stats']:  
        lista.append([user['province'],'2021-04-12',user['confirmed'],user['deaths'],user['recovered']])
    lista.pop(29)
    lista[14][0]='Estado de Mexico'
    chat_id=message.chat.id
    bot.send_message(chat_id=chat_id,text=my_message)
    for i in range(len(lista)): 
        ciudades.append(lista[i][0])
        confirmados.append(lista[i][2])
        muertes.append(lista[i][3]) 
        mensaje="""
            Ciudad: %s 
        Confirmados: %s
        Muertes: %s  
        \r"""%(ciudades[i],confirmados[i],muertes[i])
        bot.send_message(chat_id=chat_id,text=mensaje)
        
@bot.message_handler(commands=['contacto']) 
def contactos(message):
    url="github.com/Cuadernin"
    chatid=message.chat.id
    username=message.chat.first_name
    txt=f"Hola, {username}, puedes contactarme entrando a mi repositorio: {url}"
    bot.send_message(chat_id=chatid,text=txt) 

@bot.message_handler(commands=['numero']) 
def numeross(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid,text='Escribe el número: ')
    #msg=bot.reply_to(message, 'Escribe el número: ')
    bot.register_next_step_handler(msg, number)

def number(message):
    chatid=message.chat.id
    texto=message.text
    try:
        texto=int(texto)
        if texto>2 and texto<700:
            dato=numeros(texto)
            bot.send_message(chat_id=chatid,text=dato)
        else:
            #msg=bot.reply_to(message, 'ESCRIBE UN NÚMERO ENTERO MAYOR QUE 2:')
            msg=bot.send_message(chat_id=chatid, text='ESCRIBE UN NÚMERO ENTERO MAYOR QUE 2:')
            bot.register_next_step_handler(msg, number)
    except:
        #msg=bot.reply_to(message, 'ESCRIBE UN NÚMERO:')
        msg=bot.send_message(chat_id=chatid, text='Debes escribir un numero. Prueba otra vez:')
        bot.register_next_step_handler(msg, number)

@bot.message_handler(commands=['random'])
def random(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid, text='Escribe el número: ')
    bot.register_next_step_handler(msg, aleatorio)

def aleatorio(message):
    chatid=message.chat.id
    texto=message.text
    try:
        texto=int(texto)
        if texto>2 and texto<3501:
            dato=rand(texto)
            bot.send_message(chat_id=chatid,text=dato)
        else:
            #msg=bot.reply_to(message, 'ESCRIBE UN NÚMERO ENTERO MAYOR QUE 1:')
            msg=bot.send_message(chat_id=chatid, text='ESCRIBE UN NÚMERO ENTERO MAYOR QUE 1:')
            bot.register_next_step_handler(msg, aleatorio)
    except:
        #msg=bot.reply_to(message, 'ESCRIBE UN NÚMERO:')
        msg=bot.send_message(chat_id=chatid, text='Debes escribir un numero. Prueba otra vez:')
        bot.register_next_step_handler(msg, aleatorio)

@bot.message_handler(commands=['nuvo'])
def nuvo(message):
    chatbott=ChatBot('Nuvo')
    trainer=ChatterBotCorpusTrainer(chatbott)
    trainer.train("chatterbot.corpus.spanish.greetings",
    "chatterbot.corpus.spanish.conversations",
    "chatterbot.corpus.spanish.IA",
    "chatterbot.corpus.spanish.dinero",
    "chatterbot.corpus.spanish.emociones",
    "chatterbot.corpus.spanish.perfilbot")
    texto=message.text
    chatid=message.chat.id
    bot_input=chatbott.get_response(texto)
    msg=bot.send_message(chat_id=chatid,text=str(bot_input))
    bot.register_next_step_handler(msg,charla)
    return chatbott

def charla(message):
    chatbott=ChatBot('Nuvo')
    trainer=ChatterBotCorpusTrainer(chatbott)
    chatid=message.chat.id
    texto=message.text
    if texto.lower()=="salir":
        bot.send_message(chat_id=chatid,text="Hasta luego. Fue un gusto hablar contigo.")
    else:
        bot_input=chatbott.get_response(texto)
        msg=bot.send_message(chat_id=chatid,text=str(bot_input))
        bot.register_next_step_handler(msg,charla)    


while 1:
    try:
        bot.polling(none_stop = True)
    except:
        time.sleep(15)
