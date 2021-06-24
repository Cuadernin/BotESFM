from firebase import firebase
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
def conexion(chat_id,username,texto,maestro):
     ">>>>>>>>>>>>>>>>>> MANERA RAPIDA PARA INGRESAR DATOS A UNA BASE DE DATOS DE FIREBASE <<<<<<<<<<<<<<<<<<<"
     if not firebase_admin._apps:
         base=firebase.FirebaseApplication("URL",None)
         datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
         resultado=base.post(f'/Collection/{maestro}',datos)
         return resultado
     else:
         datos={"chat_id":chat_id,"Nombre":username,"mensaje":texto}
         resultado=base.post(f'/Collection/{maestro}',datos)
         return resultado
          
def lecturaR(maestro):
     ">>>>>>>>>>>>>>>>>> MANERA OPTIMA PARA SOLICITAR DATOS DE UNA BASE DE DATOS DE FIREBASE <<<<<<<<<<<<<<<<<<<"
     if not firebase_admin._apps:
         cred=credentials.Certificate('Collection')
         firebase_admin.initialize_app(cred,{'databaseURL':"URL"})
         ref=db.reference(f"/Collection/{maestro}")
         ref=ref.get()
         return ref
     else: 
         ref=db.reference(f"/Collection/{maestro}")
         ref=ref.get()
         return ref
