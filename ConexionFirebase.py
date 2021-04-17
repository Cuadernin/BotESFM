from firebase import firebase
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
def conexion(chat_id,username,texto,maestro):
    base=firebase.FirebaseApplication("https://base-8fb74-default-rtdb.firebaseio.com/",None)
    datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
    resultado=base.post(f'/profesores/{maestro}',datos)
    return resultado

def lecturaR(maestro):
    cred=credentials.Certificate('C:\\Users\\Erwin Eduardo G.C\\Documents\\PYTHON\\Bot\\base-8fb74-firebase.json')
    firebase_admin.initialize_app(cred,{'databaseURL':"https://base-8fb74-default-rtdb.firebaseio.com/"})
    ref=db.reference(f"/profesores/{maestro}")
    ref=ref.get()
    return ref

def lecturaT():
    base=firebase.FirebaseApplication("https://base-8fb74-default-rtdb.firebaseio.com/",None)
    leer=base.get('/profesores/','')
    return leer
"""
base=firebase.FirebaseApplication("https://base-8fb74-default-rtdb.firebaseio.com/",None)
    leer=base.get(f'/profesores/{maestro}','')
    """