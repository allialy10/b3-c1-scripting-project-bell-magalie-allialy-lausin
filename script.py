import pandas as pd

donnees = pd.read_csv('conso-annuelles_v1.csv',sep =';', encoding ='Latin-1')

donnees.to_csv(f'conso-clean.csv',index =False, header = True)

donnees1 = pd.read_csv('conso-clean.csv',sep =';', encoding ='Latin-1')

print(donnees1)