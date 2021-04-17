from firebase import firebase
def sug(chat_id,username,texto):
    base=firebase.FirebaseApplication("https://base-8fb74-default-rtdb.firebaseio.com/",None)
    datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
    resultado=base.post('/escuela/sugerencias',datos)
    return resultado

def lecturaSug():
    base=firebase.FirebaseApplication("https://base-8fb74-default-rtdb.firebaseio.com/",None)
    leer=base.get('/escuela/sugerencias','')
    return leer

def sugerenciasbot(chat_id,username,texto):
    base=firebase.FirebaseApplication("https://base-8fb74-default-rtdb.firebaseio.com/",None)
    datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
    resultado=base.post('/bot/sugerencias',datos)
    return resultado