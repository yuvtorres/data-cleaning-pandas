# Using Pandas for cleaning data sets and for analize it

![Primer proyecto Ironhack](https://github.com/yuvtorres/data-cleaning-pandas/blob/master/input/shark.jpg) 

Trata sobre validar una hipótesis sobre los datos 
de tiburones que se encuentrán en [kaggle](https://www.kaggle.com/teajay/global-shark-attacks).
Este se compone de dos partes:

1. Importación y limpieza de datos
2. Análisis y conclusión

## 1.Importando y limpiando los datos

Despúes de importar los datos, se buscan las celda cuyos valores son nulos.
El primer filtro se hizo por registro, contando en cada registro el número de 
valores nulos, de éste se filtran los registros que tienen todos o casi todos sus valores 
nulos, en este paso se redujo el conjunto de datos en 25723 a 6309.

No obstante el número de nulos sigue siendo elevado, y se encuentra disperso en casi
casi todos los registro. Se aplicó un filtro en cada registro que tuviera al menos un valor 
nulo. Este último filtro dió como resultado 1425 registros.

El primer tratamiendo se realizó sobre la columna "Time", obteniendo como resutlado la hora 
cuando fuera posible o el momento día en otro caso. De este análisis se creo una variable 
categórica: "moment_day"

El segundo tratamiendo se realizó sobre la columna "Fatal (Y/N)", dejando una primera 
estadística interesante: solo el 16,3 % de los ataque es fatal.

La tercer columna análizada es "Species", donde se encontrarón 21 especies para clasificar. 
Y aunque el 33% de los ataques no se logró identificar se encontrarón datos sobre el tamaño
del tiburon. De este se creo un nuevo registro.

La cuarta columna que se ha tratado ha sido Date, de esta solamente 16 regitros de 1425 quedaron sin valor.

Las últimas columnas que se han retirado del conjunto de datos antes de exportarlo son:
'Year','Date','Case Number.1', 'Case Number.2'

## 2.Análisis y conclusión

El análisis consitió en ver la evolución de los ataques reportados, pudiendo establecer un repunte
durante las decadas de los 80 y 90. Y un comportamiento estable a partir del año 2000.

También resulta llamativo el pico de los años 60's.

Respecto a la tendencia por país se puede decir que solamente tres paises: USA, Australia y Sudafrica tiene entre los 3 
el 85% de los casos.

En cuanto al comportamiento estacionario, como es de esperar, los ataques se concentran en los periodos estivales, sin importar el emisferio.

También encotramos que las especies más más peligrosas son: el tiburón blanco y el tigre, no obstante la especie queda sin determinar en una tercera parte de los ataques.

Al realizar un análisis cruzado entre países y especies, no se encontró ningún comportamiento atípico respecto a lo ya dicho:
es decir la mayoría de casos se concentran en USA y corresponde con los casos no identificados y el tiburón blanco.

Por último el análisis por actividad muestra que casi una tercera parte de los ataques se registran en surfistas. 
