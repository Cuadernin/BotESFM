from firebase import firebase
import firebase_admin
from firebase_admin import credentials

def sug(chat_id,username,texto):
    ">>>>>>>>>>>>>>>>>> MANERA SENCILLA DE INGRESAR DATOS A UNA BASE DE DATOS DE FIREBASE <<<<<<<<<<<<<<<<<<<"
    if not firebase_admin._apps:
        base=firebase.FirebaseApplication("URL",None)
        datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
        resultado=base.post('Collection',datos)
        return resultado
    else:
        datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
        resultado=base.post('Collection',datos)
        return resultado

def lecturaSug():
      ">>>>>>>>>>>>>>>>>> MANERA SENCILLA DE OBTENER DATOS DE UNA BASE DE DATOS DE FIREBASE <<<<<<<<<<<<<<<<<<<"
    if not firebase_admin._apps:
        base=firebase.FirebaseApplication("URL",None)
        leer=base.get('Collection','')
        return leer
    else:
        leer=base.get('Collection','')
        return leer

def sugerenciasbot(chat_id,username,texto):
    ">>>>>>>>>>>>>>>>>> MANERA SENCILLA DE INGRESAR DATOS A UNA BASE DE DATOS DE FIREBASE <<<<<<<<<<<<<<<<<<<"
    if not firebase_admin._apps:
        base=firebase.FirebaseApplication("URL",None)
        datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
        resultado=base.post('Collection',datos)
        return resultado
    else:
        datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
        resultado=base.post('Collection',datos)
        return resultado
