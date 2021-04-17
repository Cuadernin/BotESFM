from ConexionFirebase import lecturaR
from SugeridosFirebase import lecturaSug

def base():
    with open("BASEDEDATOS.txt","r",encoding="utf-8") as f:
        texto=f.read()
    return texto

def txtprofesores(maestro):
    leer=lecturaR(maestro)
    txt=open("profesores_ESFM.txt","w+")
    for key in leer:
        nombre=leer[key]['Nombre'].upper()
        mensaje=leer[key]['mensaje']
        mensajes=f'{nombre}: {mensaje}\n\n'
        txt.write(mensajes)
    txt.close()
    file1=open("profesores_ESFM.txt","r+")
    return file1

def txtescuela():
    leer=lecturaSug()
    txt=open("sugerencias_escuela.txt","w+")
    for key in leer:
        nombre=leer[key]['Nombre'].upper()
        mensaje=leer[key]['mensaje']
        mensajes=f'{nombre}: {mensaje}\n\n'
        txt.write(mensajes)
    txt.close()
    file2=open("sugerencias_escuela.txt","r+")
    return file2
