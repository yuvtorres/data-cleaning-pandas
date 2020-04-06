# Importing libraries
import pandas as pd
import numpy as np
import re
import datetime as dt

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
    elif  re.search(r'(?i)(bull)|(?i)(zambe)|(?i)(leucas)',x):
        return 'Bull'
    elif  re.search(r'(?i)(grey)',x):
        return 'Grey'
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
    elif  re.search(r'(?i)(dogfis)|(?i)(Spurdog)',x):
        return 'Dogfish' 
    elif  re.search(r'(?i)(Thresher)',x):
        return 'Thresher' 
    elif  re.search(r'(?i)(reef)',x):
        return 'Caribean reef' 
    elif  re.search(r'(?i)(cookis)',x):
        return 'Cookiecutter' 
    elif  re.search(r'(?i)(sevengill)',x):
        return 'Broadnose sevengill' 
    else:
        return 'Unidentified' 

def shark_size(x):
    size_m=0
    # find the size in m
    if re.search(r'[\d][\s?]+[(?i)m]|[\d]+[\.\d]+[\s?]+[(?i)m]|[\d\.\d]+[(?i)m]',x):
        size=re.findall(r'[\d][\s?]+[(?i)m]|[\d]+[\.\d]+[\s?]+[(?i)m]|[\d\.\d]+[(?i)m]',x)
        if len(size)==1:
            try:
                return float(''.join(re.findall(r'[0-9]+\.[0-9]|[0-9]',size[0])))
            except ValueError:
                print(f'el valor que no sale es {size} -> {x}')

        for i in size:
            try:
                size_m+=float(''.join(re.findall(r'[0-9]+\.[0-9]|[0-9]',i)))/len(size)
            except ValueError:
                print(f'el valor que no sale es :{i} de {size} -> {x}')

        return size_m
    #find the size in foot
    elif re.search(r'[\d]+\'',x):
        size=re.findall(r'[\d]+\'',x)
        if len(size)==1:
            try:
                return round(float(''.join(re.findall(r'[0-9]+\.[0-9]|[0-9]',size[0])))*0.3048,1)
            except ValueError:
                print(f'el valor que no sale es {size} -> {x}')
        
        for i in size:
            try:
                size_m+=float(''.join(re.findall(r'[0-9]+\.[0-9]|[0-9]',i)))/len(size)
            except ValueError:
                print(f'el valor que no sale es :{i} de {size} -> {x}')

        return round(size_m*0.3048,1)

    elif re.search(r'[\d]',x):
        print(f" lo que no se pudo -> {x}")
        return None

    else:
        return None

# To convert the column in dates
def date_format(x):

    if re.search(r'\d{2}\-\w{3}\-\d{4}|\d{1}\-\w{3}\-\d{4}',x):
        try:
            x=re.findall(r'\d{2}\-\w{3}\-\d{4}|\d{1}\-\w{3}\-\d{4}',x)
            return dt.datetime.strptime(x[0],'%d-%b-%Y')
        except ValueError:
            print(f'Error retornando en split por - -> {x}')

    if re.search(r'\d{2}\/\d{2}\/+\d{4}',x):
        try:
            x=re.findall(r'\d{2}\/\d{2}\/+\d{4}',x)
            return dt.datetime.strptime(x[0],'%d/%m/%Y')
        except ValueError:
            print(f'Error retornando en split por / -> {x}')

    if re.search(r'\d{4}-\d{2}-\d{2}',x):
        try:
            x=re.findall(r'\d{4}-\d{2}-\d{2}',x)
            return dt.datetime.strptime(x[0],'%Y-%m-%d')
        except ValueError:
            print(f'Error retornando en split por - en Y m d -> {x}')

    if re.search(r'\d{2}-\d{2}-\d{4}',x):
        try:
            x=re.findall(r'\d{2}-\d{2}-\d{4}',x)
            return dt.datetime.strptime(x[0],'%m-%d-%Y')
        except ValueError:
            print(f'Error retornando en split por - en d-m-Y -> {x}')
    
    if re.search(r'[a-zA-Z]{3}-\d{4}',x):
        try:
            x=re.findall(r'[a-zA-Z]{3}-\d{4}',x)
            return dt.datetime.strptime(x[0],'%b-%Y')
        except ValueError:
            print(f'Error retornando en split por - en Y m d -> {x}')
    
    print(f'este aun no esta {x}')
    return None
