from ConexionFirebase import lecturaR
from SugeridosFirebase import lecturaSug

def base():
    with open("BASEDEDATOS.txt","r",encoding="utf-8") as f:
        texto=f.read()
    return texto

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

def txtprofesores(maestro):
     ">>>>>>>>>>>>>>>>> SIMILAR A LA ANTERIOR FUNCION <<<<<<<<<<<<<<<<<<"
    return file1
