from ConexionFirebase import lecturaR
from SugeridosFirebase import lecturaSug

def base():
    with open("BASEDEDATOS.txt","r",encoding="utf-8") as f:
        texto=f.read()
    return texto

def txtescuela():
    leer=lecturaSug()
    txt=open("sugerencias_escuela.txt","w+")
    i=1
    for key in leer:
        #nombre=leer[key]['Nombre'].upper()
        nombre=f"Sugerencia {i}"
        mensaje=leer[key]['mensaje']
        mensajes=f'{nombre}: {mensaje}\n\n'
        txt.write(mensajes)
        i=i+1
    txt.close()
    file2=open("sugerencias_escuela.txt","r+")
    return file2

def txtprofesores(maestro):
    leer=lecturaR(maestro)
    txt=open("profesores_ESFM.txt","w+")
    i=1
    for key in leer:
        nombre=f"Reseña {i}"
        mensaje=leer[key]['mensaje']
        mensajes=f'{nombre}: {mensaje}\n\n'
        txt.write(mensajes)
        i=i+1
    txt.close()
    file1=open("profesores_ESFM.txt","r+")
    return file1


