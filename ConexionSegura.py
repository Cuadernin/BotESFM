import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred=credentials.Certificate('C:\\Users\\Erwin Eduardo G.C\\Documents\\PYTHON\\Bot\\base-8fb74-firebase.json')
firebase_admin.initialize_app(cred,{'databaseURL':"https://base-8fb74-default-rtdb.firebaseio.com/"})
ref=db.reference("/profesores/ERICK LEE GUZMÁN")
ref=ref.get()
for key in ref:
    nombre=ref[key]["Nombre"].upper()
    mensaje=ref[key]['mensaje']
    mensajes=f'{nombre}: {mensaje}\n\n'
    print(mensajes)
