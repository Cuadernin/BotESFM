import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
"""
Prueba de conexión a Firebase
"""
cred=credentials.Certificate('Collection')
firebase_admin.initialize_app(cred,{'databaseURL':"URL"})
ref=db.reference("/Collection/ERICK LEE GUZMÁN")
ref=ref.get()

    
