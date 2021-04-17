from firebase import firebase
def sug(chat_id,username,texto):
    ">>>>>>>>>>>>>>>>>> MANERA SENCILLA DE INGRESAR DATOS A UNA BASE DE DATOS DE FIREBASE <<<<<<<<<<<<<<<<<<<"
    base=firebase.FirebaseApplication("URL",None)
    datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
    resultado=base.post('Collection',datos)
    return resultado

def lecturaSug():
      ">>>>>>>>>>>>>>>>>> MANERA SENCILLA DE OBTENER DATOS DE UNA BASE DE DATOS DE FIREBASE <<<<<<<<<<<<<<<<<<<"
    base=firebase.FirebaseApplication("URL",None)
    leer=base.get('Collection','')
    return leer

def sugerenciasbot(chat_id,username,texto):
    ">>>>>>>>>>>>>>>>>> MANERA SENCILLA DE INGRESAR DATOS A UNA BASE DE DATOS DE FIREBASE <<<<<<<<<<<<<<<<<<<"
    base=firebase.FirebaseApplication("URL",None)
    datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
    resultado=base.post('Collection',datos)
    return resultado
