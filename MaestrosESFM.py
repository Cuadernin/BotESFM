from firebase import firebase
import pandas as pd
from tabulate import tabulate

def buscador(texto):
    nombres=texto.split(" ")
    nombre=nombres[0].lower()
    apellido=nombres[1].lower()
    df=pd.read_excel("ProfesoresESFMV2.xlsx")
    df=df["PROFESOR"]
    df=df.dropna()
    lista=[]
    for txt in df:
        pal=txt.lower()
        indexN=pal.find(nombre)
        indexA=pal.find(apellido)
        if indexA>=0 and indexN>=0:
            return pal.upper()
        else:
            pass

def cap(row):
    for i, item in enumerate(row):
        row[i] = item.title()
    return row

def consulta():
    df=pd.read_excel("ProfesoresESFMV2.xlsx",index_col=None)
    df=df[["PROFESOR"]]
    df=df.apply(lambda row:cap(row))
    return df
