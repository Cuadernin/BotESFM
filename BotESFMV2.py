import time
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


TOKEN=TOKEN
bot=telebot.TeleBot(TOKEN)

firebase=firebase.FirebaseApplication("link",None)

@bot.message_handler(commands=['start'])
def start(message):
    messages="""Hola😊, espero te encuentres bien. Esta es la versión 1.0 de este bot. Cualquier fallo que encuentres te agradecería muchísimo que nos contactaras. Para conocer lo que puedes hacer por favor escribe /help y lee con atención las intrucciones de uso de cada función🌞. 
    
    ¡ESPERO TE SEA DE UTILIDAD!♥
    """
    chat_id=message.chat.id # Esta instruccion  se repite muchas veces ya que con ella obtienes el id del usuario
    bot.send_message(chat_id=chat_id,text=messages) # Esta instruccion  se repite muchas veces ya que con ella mandas un mensaje al usuario del id

# ======================================= AYUDA ======================================= #
@bot.message_handler(commands=['help'])
def help(message): 
    """Crea una funcion cuando escribe HELP"""                      
    messages="Mensaje por mostrar cuando se escribe el comando /help"
    chat_id=message.chat.id  # Esta instruccion  se repite muchas veces ya que con ella obtienes el id del usuario
    bot.send_message(chat_id=chat_id,text=messages) # Esta instruccion  se repite muchas veces ya que con ella mandas un mensaje al usuario del id
 

# ======================================= PROFESORES  ======================================= # 
#### ESCRITURA DE RESEÑA ####
@bot.message_handler(commands=['profesores'])   
def profesores(message):
    chatid=message.chat.id # Esta funcion se repite muchas veces ya que con ella obtienes el id del usuario
    msg=bot.send_message(chat_id=chatid,text="Escribe el nombre del maestro empezando por el nombre:") # Esta instruccion  se repite muchas veces ya que con ella mandas un mensaje al usuario del id
    bot.register_next_step_handler(msg,profesor) # Da pie a accionar la funcion <profesor> a partir del mensaje "msg"


def profesor(message):
    lista=[]
    chatid=message.chat.id # Esta instruccion  se repite muchas veces ya que con ella obtienes el id del usuario
    texto=message.text # Esta instruccion  se repite muchas veces ya que con ella obtienes el mensaje del usuario
    maestro=buscador(str(texto))
    if maestro==None:
        msg=bot.send_message(chat_id=chatid,text="Lo siento, el profesor no existe en la base de datos. \ 
            Vuelva a escribir el nombre correctamente.") # Esta instruccion  se repite muchas veces ya que con ella mandas un mensaje al usuario del id
        bot.register_next_step_handler(msg, profesor)   
    else:
        lista.append(maestro)
        msg=bot.reply_to(message, 'Escribe tu reseña:')
        bot.register_next_step_handler(msg, escritura)   # Da pie a accionar la funcion <escritura> a partir del mensaje "msg"

def escritura(message):
    pass
        
        
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
    pass

# ======================================= PRINCIPALES  ======================================= #

# ======================================= SUGERENCIAS ======================================= #
@bot.message_handler(commands=['sugbot'])
def sugbot(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid,text="Escribe tu sugerencia:")
    bot.register_next_step_handler(msg,mibot) # Da pie a accionar la funcion <mibot> a partir del mensaje "msg"


def mibot(message):
    pass
        
# ======================================= ESCUELA  ======================================= #  
@bot.message_handler(commands=['sugerencia'])   
def sugerencia(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid,text="Escribe tu sugerencia:")
    bot.register_next_step_handler(msg,escuela) # Da pie a accionar la funcion <escuela> a partir del mensaje "msg"

def escuela(message):
    pass

@bot.message_handler(commands=['leersug'])
def leersug(message):
    chatid=message.chat.id
    texto=message.text
    txt=txtescuela()
    bot.send_document(chat_id=chatid,data=txt,caption='txt con las consultas.')  
        
@bot.message_handler(commands=['calendario'])
def calendario(message):
    ">>>>>>>>>>>>>>>>>> SIMILAR A LA FUNCION ANTERIOR <<<<<<<<<<<<<<<<<<<"
    pass

@bot.message_handler(commands=['constancias'])
def constancias(message):
    ">>>>>>>>>>>>>>>>>> SIMILAR A LA FUNCION <leersug> <<<<<<<<<<<<<<<<<<<"
    pass

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
    ">>>>>>>>>>>>>>>>>> INSERTE UNA API PARA MANDAR LA INFORMACION DE COVID <<<<<<<<<<<<<<<<<<<"
    pass
        
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
    ">>>>>>>>>>>>>>>>>> INSERTE UNA API PARA SOLICITAR DATOS DE UN NUMERO O AGRÉGUELOS CON UN YAML <<<<<<<<<<<<<<<<<<<"
    pass

@bot.message_handler(commands=['random'])
def random(message):
    chatid=message.chat.id
    msg=bot.send_message(chat_id=chatid, text='Escribe el número: ')
    bot.register_next_step_handler(msg, aleatorio) # Da pie a accionar la funcion <aleatorio> a partir del mensaje "msg"

def aleatorio(message):
    ">>>>>>>>>>>>>>>>>> INSERTE UNA API PARA SOLICITAR DATOS DE UN NUMERO O AGRÉGUELOS CON UN YAML <<<<<<<<<<<<<<<<<<<"
    pass

@bot.message_handler(commands=['nuvo'])
def nuvo(message):
    chatbott=ChatBot('Nuvo')  # Nombre del bot
    
     ">>>>>>>>>>>>>>>>>> ENTRENAMOS EL BOT <<<<<<<<<<<<<<<<<<<"
        
    texto=message.text
    chatid=message.chat.id
    bot_input=chatbott.get_response(texto) # Respuesta del bot
    msg=bot.send_message(chat_id=chatid,text=str(bot_input)) 
    bot.register_next_step_handler(msg,charla) # Da pie a accionar la funcion <charla> a partir del mensaje "msg"
    return chatbott

def charla(message):
    ">>>>>>>>>>>>>>>>>> CREAMOS UN CICLO DONDE EL BOT SIGUE LA CHARLA <<<<<<<<<<<<<<<<<<<"
    pass  

"" BLOQUE PRINCIPAL ""
while 1:
    try:
        bot.polling(none_stop = True) # Con esta instruccion garantizamos que el bot siga funcionando a pesar de errores
    except:
        time.sleep(15) # Si ocurre algun error grave esperamos 15 segundos para el reinicio
