from firebase import firebase
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
def conexion(chat_id,username,texto,maestro):
    base=firebase.FirebaseApplication("URL",None)
    datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
    resultado=base.post(f'/Collection/{maestro}',datos)
    return resultado

def lecturaR(maestro):
    cred=credentials.Certificate('Collection')
    firebase_admin.initialize_app(cred,{'databaseURL':"URL"})
    ref=db.reference(f"/Collection/{maestro}")
    ref=ref.get()
    return ref
