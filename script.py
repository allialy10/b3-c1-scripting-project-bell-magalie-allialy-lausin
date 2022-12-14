import csv

#Lecture du CSV

with open ("conso-annuelles_v1.csv", encoding = 'Latin-1') as f:


    data = csv.reader(f, delimiter=';')
    count = 0


    #Ouverture et création du fichier conso-clean en mode ecriture

    with open ('conso-clean.csv','w', encoding= 'Latin-1', newline='') as clean :

        #Création de la ligne d'entête
        
        fieldnames=['Appareil suivi','Consommation annuelle AN1','Consommation annuelle AN2','Type', 'Consommation globale']
        
        writer= csv.DictWriter(clean, fieldnames=fieldnames)
        writer.writeheader()
        

        for ligne in data:

            #Exclusion des lignes contenants des cellules vides
            if (ligne[0] != '' and ligne[1] != '' and ligne[2] != '' and ligne[3] != '' and ligne[4] != '' and ligne[3]!= '-' and count > 0) :
                
                #Conversion des consommations pour pouvoir les additionner
                ligne[2]= float(ligne[2].replace(',','.'))
                ligne[3]= float(ligne[3].replace(',','.'))


                #Addition des consommations
                e = format(ligne[2] + ligne[3], '.1f')
                

                #ecriture des lignes dans le fichier conso-clean
                writer.writerow({'Appareil suivi': ligne[0],'Consommation annuelle AN1' : ligne[2],'Consommation annuelle AN2': ligne[3],'Type' : ligne[4], 'Consommation globale' : e})
        
            count+=1
        
            
#ouverture du fichier mode lecture
with open('conso-clean.csv',newline='',encoding= 'Latin-1') as fichier_csv:
    lecteur = csv.DictReader(fichier_csv, delimiter=",")

#Trier par type et par consommation globlale par ordre décroissant

    liste_rangee = sorted(lecteur, key=lambda row:(row['Type'],float(row['Consommation globale'])), reverse=True)

#ouverture en mode écriture
with open('conso-clean.csv', 'w',newline='',encoding= 'Latin-1') as fichier_sortie:
    champs = ['Appareil suivi','Consommation annuelle AN1','Consommation annuelle AN2','Type', 'Consommation globale']
    ecriteur = csv.DictWriter(fichier_sortie, fieldnames=champs,delimiter=',',quotechar='|')
    ecriteur.writeheader()
    for ligne1 in liste_rangee:
        ecriteur.writerow(ligne1)
