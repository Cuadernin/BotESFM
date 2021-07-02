""" 
CÓDIGO COMPLETO del bot 

NOTA: Si deseas obtener los demás archivos que se usan en los diferentes comandos, contáctame al correo escrito en mi README. 
"""

import time
import requests
import telebot
import pandas as pd
import os

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from programacion import plataforma,dataset
from datos import base,txtprofesores,txtescuela
from Educacion import numeros,rand
from firebase import firebase
from tabulate import tabulate
from ConexionFirebase import conexion
from SugeridosFirebase import sug,sugerenciasbot
from MaestrosESFM import buscador,consulta
from acciones import historial
from Distribucion import distribucion,fd,grafico


TOKEN=TOKEN
bot=telebot.TeleBot(TOKEN)

firebase=firebase.FirebaseApplication("link",None)

@bot.message_handler(commands=['start'])    # Funciones que serán llamadas si el usuario escribe el comando start ---> No es necesario que la funcion se llame igual que el comando
">>>>>>>>>>>>>>>>>> A partir de aquí todo lo declarado surtirá efecto cuando se inicie el comando /start  <<<<<<<<<<<<<<<<<<<"
def start(message): # Como argumento principal de la funcion tomamos la propiedad message que tendrá en ella toda la información acerca del mensaje
    messages="""Esta es la versión 1.3 . Se han agregado tres nuevas funciones.
    1. Escudos de la escuela en formato png.
    2. Reglamento general de estudios.
    3. Solicitud de datos históricos de una acción (yahoo finance).

    Cualquier fallo que encuentres te agradecería muchísimo que me contactaras.

    ¡ESPERO TE SEA DE UTILIDAD!♥
    """
    chat_id=message.chat.id  # Esta instruccion  se repite muchas veces ya que con ella obtienes el id del usuario
    bot.send_message(chat_id=chat_id,text=messages) # Esta instruccion se repite muchas veces ya que con ella mandas un mensaje al usuario del id
    
# ======================================= AYUDA ======================================= #
@bot.message_handler(commands=['help'])  # Funciones que serán llamadas si el usuario escribe el comando help ---> No es necesario que la funcion se llame igual que el comando
""">>>>>>>>>>>>>>>>>> A partir de aquí todo lo declarado surtirá efecto cuando se inicie el comando /help (PROPIEDADES DE UNA CLASE) <<<<<<<<<<<<<<<<<<<"""

def help(message): # Como argumento principal de la funcion tomamos la propiedad message que tendrá en ella toda la información acerca del mensaje   
    
    messages="""A continuacion, la lista de funciones divididas por categorias:

===============================
========= PROFESORES ==========
===============================
    -- Escribe una reseña de un profesor:
        💬Descripción: Escribe una breve reseña de un profesor (menos de 250 carácteres).
        🔑Comando: /profesores

    -- Lee las reseñas que han escrito otros compañeros:
        💬Descripción: Lee las reseñas que han escrito otros alumnos.
        🔑Comando: /lectura

    -- Enlista los profesores disponibles en la base de datos:
        💬Descripción: Lista de profesores.
        🔑Comando: /listas

    -- Correos de los profesores:
        💬Descripción: .txt con los correos de los profesores.
        🔑Comando: /correos

================================
========= PROGRAMACIÓN ========
================================
    -- Plataformas para aprender programación:
        💬Descripción: Lista de plataformas donde se puede aprender a programar.
        🔑Comando: /plataformas
    -- Base de datos:
        💬Descripción: Cursos gratuitos de base de datos relacionales.
        🔑Comando: /cursos

===============================
========= SUGERENCIAS =========
===============================
    -- Sugerencia para mejorar el bot
        💬Descripción: Escribe una sugerencia para el autor de este bot y así seguir mejorándolo.
        🔑Comando: /sugbot

===============================
========== ESCUELA ============
===============================
    -- Escribir una sugerencia para mejorar la escuela:
        💬Descripción: Escribe una sugerencia o consejo para mejorar algún aspecto de la escuela.
        🔑Comando: /sugerencia

    -- Leer las sugerencias escritas por otros alumnos:
        💬Descripción: Puedes ver las sugerencias escritas por otros alumnos.
        🔑Comando: /leersug

    -- Plataforma para crear portadas formales (tesis, ensayos, etc):
        💬Descripción: Crea portadas formales en Latex básandote en plantillas.
        🔑Comando: /plantilla

    -- Datasets:
        💬Descripción: Sitios web donde puedes extraer datasets para usarlos en cualquier proyecto.
        🔑Comando: /datasets

    -- Solicitar constancias oficiales:
        💬Descripción: PowerPoint con las instrucciones oficiales para solicitar una constancia.
        🔑Comando: /constancias

    -- Escudos del IPN y ESFM:
        💬Descripción: Escudos del IPN y ESFM en formato png.
        🔑Comando: /escudo

    -- Calendario del IPN:
        💬Descripción: Calendario oficial del IPN.
        🔑Comando: /calendario

    -- Reglamento del IPN:
        💬Descripción: Reglamento general de estudios.
        🔑Comando: /reglamento

    -- Certificados y carta de pasante:
        💬Descripción: Procedimiento para obtener el certificado de estudios y la carta de pasante.
        🔑Comando: /certificado

    -- Denuncias:
        💬Descripción: Procedimiento para realizar una denuncia
        🔑Comando: /denuncia


===============================
=========== OTROS =============
===============================
    -- Covid:
        💬Descripción: Confirmados y muertes por estado en México.
        🔑Comando: /covid

    -- Datos históricos de una acción:
        💬Descripción: Solicita los datos históricos de una acción que cotice en USA (yahoo financie).
        🔑Comando: /acciones

    -- Datos matemáticos acerca de un número:
        💬Descripción: Datos matemáticos acerca de un número ENTERO que escribas (válido desde el 3 al 700).
        🔑Comando: /numero

    -- Datos interesantes acerca de un número:
        💬Descripción: Datos interesantes sobre un número ENTERO que escribas(válido del 1 al 3500).
        🔑Comando: /random

    -- Contacto:
        💬Descripción: Repertorio del proyecto.
        🔑Comando: /contacto

    -- Distribución de datos:
        💬Descripción: Encuentra la mejor distribución que se adapte a los datos.
        🔑Comando: /distr

    -- ChatBot:
        💬Descripción: Chatea con un chatbot llamado Nuvo.
        🔑Comando: /nuvo
        📑Nota: Este es el primer chatbot que diseño llamado Nuvo👷. Para dejar de hablar con él escribe: salir.
    """  # Mensaje por mostrar cuando se escribe el comando /help
    
    chat_id=message.chat.id  # Esta instruccion  se repite muchas veces ya que con ella obtienes el id del usuario
    bot.send_message(chat_id=chat_id,text=messages) # Esta instruccion se repite muchas veces ya que con ella mandas un mensaje al usuario del id
 
# ======================================= PROFESORES  ======================================= # 
#### ESCRITURA DE RESEÑA ####
@bot.message_handler(commands=['profesores'])    # Funciones que serán llamadas si el usuario escribe el comando profesores ---> No es necesario que la funcion se llame igual que el comando
def profesores(message): # Como argumento principal de la funcion tomamos la propiedad message que tendrá en ella toda la información acerca del mensaje
    chatid=message.chat.id # Esta funcion se repite muchas veces ya que con ella obtienes el id del usuario
    msg=bot.send_message(chat_id=chatid,text="Escribe el nombre del maestro empezando por el nombre:") # Esta instruccion se repite muchas veces ya que con ella mandas un mensaje al usuario del id
    bot.register_next_step_handler(msg,profesor) # Da pie a accionar la funcion <profesor> a partir del mensaje "msg"

lista=[]
def profesor(message):
    chatid=message.chat.id # Esta instruccion se repite muchas veces ya que con ella obtienes el id del usuario
    texto=message.text # Esta instruccion se repite muchas veces ya que con ella obtienes el mensaje del usuario
    maestro=buscador(str(texto))
    if maestro==None:
        msg=bot.send_message(chat_id=chatid,text="Lo siento, el profesor no existe en la base de datos. \ 
            Vuelva a escribir el nombre correctamente.") # Esta instruccion se repite muchas veces ya que con ella mandas un mensaje al usuario del id
        bot.register_next_step_handler(msg, profesor)   
    else:
        lista.append(maestro)
        msg=bot.reply_to(message, 'Escribe tu reseña:')
        bot.register_next_step_handler(msg, escritura)   # Da pie a accionar la funcion <escritura> a partir del mensaje "msg"

def escritura(message):
    try:
        chatid=message.chat.id
        texto=message.text
        if len(texto)<250 and len(texto)>0:
            if message.chat.last_name==None:
                username=message.chat.first_name
            else:
                username=message.chat.first_name+'_'+message.chat.last_name
            respuesta=conexion(chatid, username,texto,lista[0])
            lista.pop(0)
            if respuesta==1: msg=bot.send_message(chat_id=chatid,text=f'Muchas gracias, {username}.')
            else: msg=bot.send_message(chat_id=chatid,text=f'Tal vez el servidor esta dormido.')
        elif len(texto)<16 and len(texto)>0:
            msg=bot.send_message(chat_id=chatid,text='Trata de escribir algo serio. Prueba otra vez.')
            bot.register_next_step_handler(msg, escritura)
        else:
            msg=bot.send_message(chat_id=chatid,text='El texto debe contener más de 16 y menos de 250 carácteres. Prueba otra vez:')
            bot.register_next_step_handler(msg,escritura)
    except Exception as e:
        bot.send_message(chat_id=message.chat.id,text="Algo raro paso. Lo siento.")      
        
#### LECTURA DE RESEÑA #### 
@bot.message_handler(commands=['listas'])
def listas(message):
    chatid=message.chat.id
    texto=consulta()
    text=texto[:80]
    txt=tabulate(text,headers=["Id","PROFESOR"])  # Esta instruccion permite imprimir de forma bonita un dataframe
    bot.send_message(chat_id=chatid,text=txt,parse_mode="Markdown")
    texto2=texto[80:]
    txt2=tabulate(texto2,headers=["Id","PROFESOR"])
    bot.send_message(chat_id=chatid,text=txt2,parse_mode="Markdown")
    

@bot.message_handler(commands=['lectura'])
def lectura(message):
    chatid=message.chat.id
    texto=message.text
    msg=bot.send_message(chat_id=chatid,text="Escribe el nombre del maestro empezando por el nombre:")
    bot.register_next_step_handler(msg,validado) # Da pie a accionar la funcion <validado> a partir del mensaje "msg"

def validado(message):
    chatid=message.chat.id
    texto=message.text
    if len(texto)>1:
        nombres=texto.split(" ")
        if len(nombres)>1:
            maestro=buscador(str(texto))
            if maestro==None:
                msg=bot.send_message(chat_id=chatid,text="Lo siento, el profesor no existe en la base de datos. Vuelva a escribir el nombre correctamente:")
                bot.register_next_step_handler(msg, validado)
            else:
                txt=txtprofesores(maestro)
                bot.send_document(chat_id=chatid,data=txt,caption='.txt con las consultas.')
        else:
            msg=bot.send_message(chat_id=chatid,text="Ingresa un NOMBRE y APELLIDO o el nombre completo del profesor:")
            bot.register_next_step_handler(msg, validado)
    else:
         msg=bot.send_message(chat_id=chatid,text="Escribe un nombre de profesor válido (nombre y apellido). Vuelva a escribir el nombre correctamente:")
         bot.register_next_step_handler(msg, validado)


# ======================================= SUGERENCIAS ======================================= #
@bot.message_handler(commands=['sugbot'])
def sugbot(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid,text="Escribe tu sugerencia:")
    bot.register_next_step_handler(msg,mibot) # Da pie a accionar la funcion <mibot> a partir del mensaje "msg"

def mibot(message):
    try:
        chatid=message.chat.id
        texto=message.text
        if len(texto)<250 and len(texto)>1:
            if message.chat.last_name==None:
               username=message.chat.first_name
            else:
                username=message.chat.first_name+'_'+message.chat.last_name
            respuesta=sugerenciasbot(chatid,username,texto)
            if respuesta==1:
                msg=bot.send_message(chat_id=chatid,text=f'Muchas gracias, {username}, por tu sugerencia. Esto me ayuda a mejorar el bot.')
            else:
                msg=bot.send_message(chat_id=chatid,text=f'Tal vez el servidor esta dormido.')
        elif len(texto)<16 and len(texto)>1:
            msg=bot.send_message(chat_id=chatid,text='Trata de escribir algo serio. Prueba otra vez.')
            bot.register_next_step_handler(msg,mibot)
        else:
            msg=bot.send_message(chat_id=chatid,text='El texto debe contener más de 16 carácteres y menos de 250. Prueba otra vez.')
            bot.register_next_step_handler(msg,mibot)
    except Exception as e:
        bot.send_message(chat_id=message.chat.id,text="Algo raro paso. Lo siento.")
        print(e)
        
# ======================================= ESCUELA  ======================================= #  
@bot.message_handler(commands=['sugerencia'])   
def sugerencia(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid,text="Escribe tu sugerencia:")
    bot.register_next_step_handler(msg,escuela) # Da pie a accionar la funcion <escuela> a partir del mensaje "msg"

def escuela(message):
    try:
        chatid=message.chat.id
        texto=message.text
        if len(texto)<250 and len(texto)>1:
            if message.chat.last_name==None:
                username=message.chat.first_name
            else:
                username=message.chat.first_name+'_'+message.chat.last_name
            respuesta=sug(chatid, username,texto)
            if respuesta==1:
                msg=bot.send_message(chat_id=chatid,text=f'Muchas gracias, {username}.')
            else:
                msg=bot.send_message(chat_id=chatid,text=f'Tal vez el servidor esta dormido')
        elif len(texto)<16 and len(texto)>1:
            msg=bot.send_message(chat_id=chatid,text='Trata de escribir algo serio. Prueba otra vez.')
            bot.register_next_step_handler(msg, escuela)
        else:
            #msg=bot.reply_to(message, 'El texto debe contener menos de 250 caracteres. Prueba otra vez')
            msg=bot.send_message(chat_id=chatid,text='El texto debe contener más de 16 carácteres y menos de 250. Prueba otra vez.')
            bot.register_next_step_handler(msg, escuela)
    except Exception as e:
        bot.send_message(chat_id=message.chat.id,text="Algo raro paso. Lo siento.")
        print(e)

@bot.message_handler(commands=['leersug'])
def leersug(message):
    chatid=message.chat.id
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

@bot.message_handler(commands=["datasets"])
def datasets(message):
    chatid=message.chat.id
    texto=dataset()
    bot.send_message(chat_id=chatid,text=texto)

@bot.message_handler(commands=["denuncia"])
def denuncia(message):
    chatid=message.chat.id
    texto="Puedes emitir tu denuncia a través del siguiente link: https://www.denunciasegura.ipn.mx/"
    bot.send_message(chat_id=chatid,text=texto)
    texto="Además, puedes emitir una queja a través del siguiente link: https://www.ipn.mx/defensoria/orientacion-queja/queja.html"
    bot.send_message(chat_id=chatid,text=texto)
    
@bot.message_handler(commands=["reglamento"])
def reglamento(message):
    chatid=message.chat.id
    url="Reg_General_Estudios.pdf"
    with open(url,'rb') as file:
        bot.send_document(chat_id=chatid,data=file,caption='Reglamento General de Estudios')

@bot.message_handler(commands=["escudo"])
def logos(message):
    chatid=message.chat.id
    with open("ESCUDO_ESFM.png",'rb') as file:
        bot.send_photo(chat_id=chatid,photo=file)
    with open("ipn.png",'rb') as file:
        bot.send_photo(chat_id=chatid,photo=file)
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
        'x-rapidapi-key':"key",
        'x-rapidapi-host':"host"
        }
    response=requests.request("GET",link,headers=headers, params=querystring)
    data=response.json()
    my_message="""Hola, espero se encuentre bien. A continuación, la información acumulada de COVID-19 en el pais."""
    chat_id=message.chat.id
    bot.send_message(chat_id=chat_id,text=my_message)
    for user in data['data']['covid19Stats']:
        lista.append([user['province'],user['confirmed'],user['deaths']])
        if user['province']!="Unknown":
            mensaje="""
            **** %s ****
            Confirmados: %s
            Muertes: %s
            \r"""%(user["province"],user["confirmed"],user["deaths"])
            bot.send_message(chat_id=chat_id,text=mensaje)
        
@bot.message_handler(commands=['contacto']) 
def contactos(message):
    url="github.com/Cuadernin"
    chatid=message.chat.id
    username=message.chat.first_name # Esta instruccion  te permite obtener el nombre del usuario
    txt=f"Hola, {username}, puedes contactarme entrando a mi repositorio: {url}"
    bot.send_message(chat_id=chatid,text=txt) 

@bot.message_handler(commands=['numero']) 
def numeross(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid,text='Escribe el número: ')
    bot.register_next_step_handler(msg, number) # Da pie a accionar la funcion <number> a partir del mensaje "msg"

def number(message):
    chatid=message.chat.id
    texto=message.text
    try:
        texto=int(texto)
        if texto>2 and texto<700:
            dato=numeros(texto)
            bot.send_message(chat_id=chatid,text=dato)
        else:
            msg=bot.send_message(chat_id=chatid, text='ESCRIBE UN NÚMERO ENTERO MAYOR QUE 2:')
            bot.register_next_step_handler(msg, number)
    except:
        msg=bot.send_message(chat_id=chatid, text='Debes escribir un número entero. Prueba otra vez:')
        bot.register_next_step_handler(msg, number)

@bot.message_handler(commands=['random'])
def random(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid, text='Escribe el número: ')
    bot.register_next_step_handler(msg, aleatorio) # Da pie a accionar la funcion <aleatorio> a partir del mensaje "msg"

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
            msg=bot.send_message(chat_id=chatid, text='ESCRIBE UN NÚMERO ENTERO MAYOR QUE 2:')
            bot.register_next_step_handler(msg, aleatorio)
    except:
        #msg=bot.reply_to(message, 'ESCRIBE UN NÚMERO:')
        msg=bot.send_message(chat_id=chatid, text='Debes escribir un número entero. Prueba otra vez:')
        bot.register_next_step_handler(msg, aleatorio)

@bot.message_handler(commands=['nuvo'])
def nuvo(message):
    chatid=message.chat.id
    mensaje='Para empezar a usarlo escribe Hola. Escribe Salir cuando desees dejar de hablar con él.'
    msg=bot.send_message(chat_id=chatid,text=mensaje)
    bot.register_next_step_handler(msg,inicio)

def inicio(message):
    try:
        chatid=message.chat.id
        chatbott=ChatBot('Nuvo',storage_adapter='chatterbot.storage.SQLStorageAdapter',
        preprocessors=['chatterbot.preprocessors.clean_whitespace',],
        logic_adapters=[{
            'import_path':'chatterbot.logic.BestMatch',
            'default_response':'Lo siento, no puedo entender lo que dices :c.',
            'maximum_similarity_threshold':0.90,},'chatterbot.logic.MathematicalEvaluation'],
        database_uri='sqlite:///database.db',read_only=True)
        """
        trainer=ChatterBotCorpusTrainer(chatbott)
        trainer.train("chatterbot.corpus.spanish.greetings",
        "chatterbot.corpus.spanish.conversations",
        "chatterbot.corpus.spanish.IA",
        "chatterbot.corpus.spanish.dinero",
        "chatterbot.corpus.spanish.emociones",    Se anula esta parte porque ya lo entrene una vez y dicho entrenamiento se guarda
        "chatterbot.corpus.spanish.perfilbot",      en database.db.
        "chatterbot.corpus.spanish.greetings",    Si deseo entrenarlo con nueva información debo volver a colocar esta parte comentada
        "chatterbot.corpus.spanish.psicologia")
        """
        texto=message.text
        chatid=message.chat.id
        bot_input=chatbott.get_response(texto)
        msg=bot.send_message(chat_id=chatid,text=str(bot_input))
        bot.register_next_step_handler(msg,charla)
    except Exception as e:
        print(e)

def charla(message):
    chatbott=ChatBot('Nuvo',storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors=['chatterbot.preprocessors.clean_whitespace',],
    logic_adapters=[{
        'import_path':'chatterbot.logic.BestMatch',
        'default_response':'Lo siento, no puedo entender lo que dices :c.',
        'maximum_similarity_threshold':0.90,},'chatterbot.logic.MathematicalEvaluation'],
    database_uri='sqlite:///database.db',read_only=True)
    chatid=message.chat.id
    texto=message.text
    if texto.lower()=="salir":
        bot.send_message(chat_id=chatid,text="Hasta luego. Fue un gusto hablar contigo.")
    else:
        bot_input=chatbott.get_response(texto)
        msg=bot.send_message(chat_id=chatid,text=str(bot_input))
        bot.register_next_step_handler(msg,charla)
        
lista2=[]
@bot.message_handler(commands=["acciones"])
def stocks(message):
    mensaje="""No olvides tomar en cuenta cuándo la empresa comenzó a cotizar en la bolsa o de lo contrario no te generará el archivo. Ejemplo de uso:
        Abreviatura: FB
        Fecha de inicio: 27-03-2020 (sin espacios)
        Fecha de fin: 28-03-2021 (sin espacios)
        """
    chatid=message.chat.id
    bot.send_message(chat_id=chatid,text=mensaje)
    msg=bot.send_message(chat_id=chatid,text="Escribe la abreviatura:")
    bot.register_next_step_handler(msg,fecha1)

def fecha1(message):
    texto=message.text
    if len(texto)>1:
        lista2.append(texto)
        chatid=message.chat.id
        msg=bot.send_message(chat_id=chatid,text="Escribe la fecha de inicio:")
        bot.register_next_step_handler(msg,fecha2)
    else:
        msg=bot.send_message(chat_id=chatid,text='Escribe una fecha válida. Prueba otra vez.')
        bot.register_next_step_handler(msg,fecha1)

def fecha2(message):
    texto=message.text
    guion=texto.find("-")
    if len(texto)>=8 and len(texto)<=10 and guion!=-1:
        lista2.append(texto)
        chatid=message.chat.id
        msg=bot.send_message(chat_id=chatid,text="Escribe la fecha de fin:")
        bot.register_next_step_handler(msg,stock)
    else:
        msg=bot.send_message(chat_id=chatid,text='Escribe una fecha válida. Prueba otra vez.')
        bot.register_next_step_handler(msg,fecha2)

def stock(message):
    texto=message.text
    chatid=message.chat.id
    guion=texto.find("-")
    if len(texto)>=8 and len(texto)<=10 and guion!=-1:
        lista2.append(texto)
        ac=historial(lista2[0],lista2[1],lista2[2])
        if ac==1:
            with open('valores_acciones.csv','rb') as file:
                bot.send_document(chat_id=chatid,data=file,caption='csv con los datos.')
                lista2.clear()
        else:
            bot.send_message(chat_id=chatid,text='Algo falla, intenta con otra abreviatura o cambia la fecha.')
    else:
        msg=bot.send_message(chat_id=chatid,text='Escribe una fecha válida. Prueba otra vez.')
        bot.register_next_step_handler(msg,stock)

@bot.message_handler(commands=["distr"])
def distr(message):
    mensaje="""CARGA el csv (menos de 20 MB)"""
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid,text=mensaje)
    bot.register_next_step_handler(msg,carga)

nombres=[]
def carga(message):
    try:
        dir=os.getcwd()
        fileid=message.document.file_id
        nombre=message.document.file_name
        nombres.append(nombre)
        chatid=message.chat.id
        file=bot.get_file(fileid)
        downf=bot.download_file(file.file_path)
        with open(dir + "/" + nombre,'wb') as f:
            f.write(downf)
        msg=bot.send_message(chat_id=chatid,text="Escribe el nombre de la columna:")
        bot.register_next_step_handler(msg,doc)
    except Exception as e:
        bot.send_message(chat_id=chatid,text=str(e))
        print(e)

def doc(message):
    texto=message.text
    chatid=message.chat.id
    if len(texto)>1:
        try:
            data=pd.read_csv(nombres[0],encoding="latin1")
            result=distribucion(data[texto])
            mensaje="""
        Distribución escogida: %s

        Valor p: %s

        Parametros: %s
            """%(result[0],result[1],result[2])
            bot.send_message(chat_id=chatid,text=mensaje)
            pdf=fd(result[3],result[2])
            grafico(data,texto,pdf,result)
            with open("distribucion.png",'rb') as file:
                bot.send_photo(chat_id=chatid,photo=file)
        except Exception as e:
            print(e)

""" BLOQUE PRINCIPAL """
while 1:
    try:
        bot.polling(none_stop = True) # Con esta instruccion garantizamos que el bot siga funcionando a pesar de errores
    except:
        time.sleep(15) # Si ocurre algun error grave esperamos 15 segundos para el reinicio
