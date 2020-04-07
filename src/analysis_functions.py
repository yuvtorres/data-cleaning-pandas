# Importing libraries
import pandas as pd
import numpy as np
import re
import datetime as dt

def make_heatmap(country,species,df_cs2):
    result=[]
    k_i=0
    s_i=0
    for k in country:
        inner=[]
        for s in species:
            if (k,s) in df_cs2.index:
                inner.append(df_cs2.loc[(k,s)][0])
            else:
                inner.append(0)
            s_i+=1
        k_i+=1
        result.append(inner)

    return result
