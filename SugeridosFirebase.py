from firebase import firebase
def sug(chat_id,username,texto):
    base=firebase.FirebaseApplication("URL",None)
    datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
    resultado=base.post('Collection',datos)
    return resultado

def lecturaSug():
    base=firebase.FirebaseApplication("URL",None)
    leer=base.get('Collection','')
    return leer

def sugerenciasbot(chat_id,username,texto):
    base=firebase.FirebaseApplication("URL",None)
    datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
    resultado=base.post('Collection',datos)
    return resultado
