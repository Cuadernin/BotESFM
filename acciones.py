import pandas_datareader.data as web
import datetime
import requests_cache

def historial(accion,fecha_start,fecha_end):
    expire_after=datetime.timedelta(days=3)
    session=requests_cache.CachedSession(cache_name='cache',backend='sqlite',expire_after=expire_after)
    fecha_start=fecha_start.split("-")
    fecha_end=fecha_end.split("-")
    try:
        start=datetime.datetime(int(fecha_start[2]),int(fecha_start[1]),int(fecha_start[0]))
        end=datetime.datetime(int(fecha_end[2]),int(fecha_end[1]),int(fecha_end[0]))
        result=web.DataReader(accion,'yahoo',start,end,session=session)
        result.to_csv('valores_acciones.csv')
        return 1
    except Exception as e:
        return 0