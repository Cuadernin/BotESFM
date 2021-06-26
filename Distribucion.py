import warnings
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
def distribucion(data):
    """
    Se elige la prueba de Kolmogorov-Smirnov ya que al ser "no parametrica" se adapta a
    los datos con el fin de no suponer que el conjunto sigue una determinada distribución y
    así determinar si dos muestras (obviamente cuanto más grandes mucho mejor) tienen la misma
    distribución de datos.

    Contraste de hipótesis:
        H_0: El conjunto de dato sigue la misma distribución
        H_a: El conjunto de datos tiene una diferente distribución

    Tomando un nivel de significancia del 5%, es decir, alpha=0.05 (intervalo de confianza del 95%)
    y usando el valor p, la hipótesis se ve como:
        H_0: P>0.05  ------------------> Aceptamos H_0 y podemos concluir (con un 95% de prob. ) que sigue la misma distribución
        H_a: P<=0.05 ------------------> Rechazamos H_0

    En nuestro caso, usaremos el valor p más grande para determinar cuál de todas las distribuciones se adapta mejor a
    los datos.
    """
    distr=['bradford',"arcsine","anglit","argus","norm", "exponweib", "weibull_max", "weibull_min", "pareto", "uniform","t","expon","vonmises",
    "burr","burr12","crystalball","dgamma","dweibull","erlang","exponnorm","exponweib","fisk","foldnorm","johnsonsu","logistic","pearson3","powernorm",
    "gumbel_r","gumbel_l","halfnorm","invgauss","invgamma","kappa3","maxwell","ncf","nct","nakagami","levy","rice","truncnorm","wrapcauchy",
    "lognorm","beta","cauchy","f","chi2","laplace","gamma","chi","genpareto","genexpon","invgamma","johnsonsb",
    "genextreme","gausshyper","gilbrat","gompertz","wald","rdist","rayleigh","vonmises","pearson3","ncx2","lomax","moyal","mielke","logistic",
    "loggamma","johnsonsu","dweibull","fatiguelife","frechet_l"]
    parametros={};resultados=[]
    for dist_name in distr:
        dist=getattr(st, dist_name) #extraemos los atributos de cada distribucion almacenados en la libreria scipy
        parametro=dist.fit(data) #ajustamos los datos
        parametros[dist_name]=parametro #igualamos los parametros de cada distribucion a la variable ----> parametro
        estadistico,p_valor=st.kstest(data,dist_name,args=parametro)# Aplicamos la prueba de Kolmogorov-Smirnov
        resultados.append([dist_name,p_valor,dist])

    dist_escogida,p_value,dist=(max(resultados,key=lambda item:item[1])) #se extrae la distribucion con el valor p mas grande
    return dist_escogida,p_value,parametros[dist_escogida],dist

def fd(distr,params,n=9800):
    """ Funcion de densidad de la distribucion"""
    args=params[:-2];loc=params[-2];scale=params[-1]

    liz=distr.ppf(0.01,*args,loc=loc,scale=scale) if args else distr.ppf(0.01,loc=loc,scale=scale)
    ldr=distr.ppf(0.99,*args,loc=loc,scale=scale) if args else distr.ppf(0.99,loc=loc,scale=scale)
    x=np.linspace(liz,ldr,n)
    data=distr.pdf(x,loc=loc,scale=scale,*args)

    return pd.Series(data,x)

def grafico(data,columna,pdf,result):
    plt.figure(figsize=(12,8))
    xmin,xmax=plt.xlim()
    plt.hist(data[columna],bins=25,density=1,alpha=0.6,color='g',label='Histograma con distribución')
    ax=pdf.plot(lw=2, label=result[0],legend=True)
    plt.savefig('distribucion.png')
