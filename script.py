import pandas as pd

import numpy as np

# Lecture d'un ficher 


donnees = pd.read_csv('conso-annuelles_v1.csv',sep =';', encoding ='Latin-1')

# Création d'un fichier csv à partir du csv original

donnees.to_csv(f'conso-clean.csv',index =False, sep= ';', header = True, na_rep="")

donnees1 = pd.read_csv('conso-clean.csv',sep =';', encoding ='Latin-1')


print((donnees1))
