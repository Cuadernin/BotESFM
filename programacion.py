def plataforma():
     """>>>>>>>>>>>>>>>>>> SIMPLE LECTURA DE ARCHIVO TXT <<<<<<<<<<<<<<<<<<<"""
    with open("Programacion.txt","r",encoding="utf-8") as f:
        texto=f.read()
    return texto

def dataset():
    with open("DATASETS.txt","r",encoding="utf-8") as f:
        texto=f.read()
    return texto
