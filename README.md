# Using Pandas for cleaning data sets and for analize it

Primer proyecto Ironhack

Trata sobre validar una hipótesis sobre los datos 
de tiburones que se encuentrán en [kaggle](https://www.kaggle.com/teajay/global-shark-attacks).
Este se compone de dos partes:

1. Importación y limpieza de datos
2. Análisis y conclusión

## 1.Importando y Limpiando los datos

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






