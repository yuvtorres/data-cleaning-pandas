# Importing libraries
import pandas as pd
import numpy as np
import re

#Define la nueva columna con el valor númerico donde no pone -1
def promedio_hora(vector_hora):
    vector=[int(x[:-1]) for x in vector_hora]
    return int(sum(vector)/len(vector)) if len(vector)>0 else -1

#Cuando encuentra una celda con digitos, la convierte en cadena de carácteres

def limpia_comillas_corchetes(x):
    if x==[]:
        return None
    else:
        x=str(x).replace('[','').replace(']','').replace("'","")
        return x

# convierte las cadenas a horas
def f_hora_con_ceros(x):
    if x == None:
        return None
    else:
        if x[1].isdigit():
            return int(x[0:2])
        else:
            return int(str(x[0]))

# crea variable Momento del Día
def moment_day(x):
    if isinstance(x,str):
        return x
    elif x is not None:
        x=int(x)
        if x>5 and x<13:
            return "Morning"
        elif x<19 and x>12:
            return "Afternoon"
        elif (x>-1 and x <6) or (x>18):
            return "Night"
    else:
        return x

def fatal_clasification(x):
      if 'N' in x:
          return False
      elif 'Y' in x:
          return True
      else:
          return None

def shark_species(x):
    if  re.search(r'(?i)(ragged|sand)',x):
        return 'Ragged Tooth'
    elif re.search(r'(?i)(white)',x):
        return 'White'
    elif re.search(r'(?i)(tiger)',x):
        return 'Tiger'
    elif  re.search(r'(?i)(bull)',x):
        return 'Bull'
    elif  re.search(r'(?i)(grey)',x):
        return 'Grey'
    elif  re.search(r'(?i)(zambes)',x):
        return 'Zambesi'
    elif  re.search(r'(?i)(gangetic)',x):
        return 'Ganges'
    elif  re.search(r'(?i)(wobbegong)',x):
        return 'Wobbegong'
    elif  re.search(r'(?i)(Mako)',x):
        return 'Mako'
    elif  re.search(r'(?i)(hammerhead)',x):
        return 'Hammerhead'
    elif  re.search(r'(?i)(urse)',x):
        return 'Nurse'
    elif  re.search(r'(?i)(Copper|Whaler|narrowtooth)',x):
        return 'Copper'
    elif  re.search(r'(?i)(blacktip)',x):
        return 'Blacktip'
    elif  re.search(r'(?i)(blue)',x):
        return 'Blue'
    elif  re.search(r'(?i)(spinner)',x):
        return 'Spinner' 
    elif  re.search(r'(?i)(galapago)',x):
        return 'Galapagos' 
    elif  re.search(r'(?i)(dusky)',x):
        return 'Dusky' 
    elif  re.search(r'(?i)(lem+on)',x):
        return 'Lemmon' 
    else:
        return x 


