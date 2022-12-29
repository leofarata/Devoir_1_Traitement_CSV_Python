import os
import csv

fichier_csv = "fichier_csv.csv" #Le fichier CSV a charger

header = ["nom", "prenom", "age", "ville"] #L'entete du fichier CSV

if(os.path.isfile(fichier_csv) == False):
    begin = open (fichier_csv, "w")
    begin.close()

if(os.stat(fichier_csv).st_size == 0):
    with open (fichier_csv, "a", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(header)
         
#Fonction pour afficher toutes les personnes enregistrées ===========================

def Afficher_Personnes(fichier_csv):
    with open (fichier_csv, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print()
        print("#|-- nom --|-- prenom --|-- age --| ville --|#")
        for line in csv_reader:
            print()
            print("| {nom} | {prenom} | {age} | {ville} |".format(nom=line['nom'],prenom=line['prenom'],age=line['age'],ville=line['ville']))

    return 


#Fonction pour ajouter une nouvelle personne ===========================

def Ajouter_Nouvelle_Pernonne(fichier_csv):
    nom = ""
    prenom = ""
    age = ""
    ville = ""

    print()
    print("------ Ajouter une personne ------")
    print()

    while (nom == "" or nom.isnumeric()):
        nom = input("Saisissez votre nom: ")
        
        if(nom == ""):
            print()
            print("Vous ne devez pas laisser le champ vide")
            print()
        elif(nom.isnumeric()):
            print()
            print("Les valeurs numeriques ne sont pas acceptées")
            print()
        else:
            break

    while (prenom == "" or prenom.isnumeric()):
        prenom = input("Saisissez votre prenom: ")
        
        if(prenom == ""):
            print()
            print("Vous ne devez pas laisser le champ vide")
            print()
        elif(prenom.isnumeric()):
            print()
            print("Les valeurs numeriques ne sont pas acceptées")
            print()
        else:
            break

    while (age.isnumeric() == False):
           age = input("Saisissez votre age: ")
           if(age.isnumeric() == False):
              print()
              print("Vous devez saisir un nombre ou un chiffre")
              print()

    while (ville == "" or ville.isnumeric()):
        ville = input("Saisissez votre ville: ")
        
        if(ville == ""):
            print()
            print("Vous ne devez pas laisser le champ vide")
            print()
        elif(ville.isnumeric()):
            print()
            print("Les valeurs numeriques ne sont pas acceptées")
            print()
        else:
            break
              
    with open (fichier_csv, "a", newline="") as csv_file:
         writer = csv.writer(csv_file, delimiter=",")
         writer.writerow([nom, prenom, age, ville])
         print()
         print("Personne ajoutée avec SUCCES")
         
    return 



#Fonction pour modifier les informations d'une personne ===========================
def Modifier_Infos_Personne(fichier_csv):
    nom_personne = ""
    Info_Personne = {}
    Base_Donnes = {}
    Donnees = []
    with open (fichier_csv, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for line in csv_reader:
            Base_Donnes[line["nom"]] = line

      
        while (nom_personne == "" or nom_personne in Base_Donnes):
          print()
          print("------ Modifier une personne ------")
          print("1, Retour en Arriere")
          print() 
          nom_personne = input("Saisissez le nom de la personne a modifier: ")
          if(nom_personne == ""):
              print()
              print("Vous ne devez pas laisser le champ vide")
              print()
          elif(nom_personne == "1"):
              break
          elif(nom_personne not in Base_Donnes):
              print()
              print("La Personne n'exite pas, saisissez le nom d'une personne qui existe")
              print()
          
          else:
          
            Info_Personne = Base_Donnes[nom_personne]
              

            if(Info_Personne != {}): #Si la personne à été trouvé
                menu = ["nom","prenom","age","ville"]
                infoAModifier = ""
                
                while (infoAModifier not in {"1","2","3","4"}):
                    print()
                    print("1, nom")
                    print("2, prenom")
                    print("3, age")
                    print("4, ville")
                    print()
                    infoAModifier = input("Quel information souhaitez vous modifier ? ")

                    if(infoAModifier not in {"1","2","3","4"}):
                        print()
                        print("Votre saisie doit etre comprise entre 1, 2, 3 ou 4")

                    else:
                        infoAModifier = menu[int(infoAModifier)-1]
                        break

                infoNouvelleValeur = ""
                while infoNouvelleValeur == "" or infoNouvelleValeur.isnumeric():
                    infoNouvelleValeur = input("Renseigner la nouvelle valeur de \"" + infoAModifier +"\": ")
                    if(infoNouvelleValeur == ""):
                        print()
                        print("Le champ ne doit pas rester vide")
                        print()
                    elif(infoNouvelleValeur.isnumeric()):
                        print()
                        print("Les valeurs numeriques ne sont pas acceptéss")
                        print()
                    else:
                        break
                      
                Info_Personne[infoAModifier] = infoNouvelleValeur
                Base_Donnes[nom_personne] = Info_Personne
                
                for elem in Base_Donnes:
                    Donnees.append(Base_Donnes[elem])
    
                with open (fichier_csv, "w", newline="") as csv_file:
                    csv_reader = csv.DictWriter(csv_file, fieldnames = header)
                    csv_reader.writeheader()
                    csv_reader.writerows(Donnees)
                    print()
                    print("Personne modifiée avec SUCCES")
                    break
                        
        
    return


#Fonction pour supprimer une personne ===========================
def Supprimer_Personne(fichier_csv):
    nom_personne = ""
    #Info_Personne = {}
    Base_Donnes = {}
    Donnees = []
    with open (fichier_csv, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for line in csv_reader:
            Base_Donnes[line["nom"]] = line

        while (nom_personne == "" or nom_personne in Base_Donnes):
          print()
          print("------ Supprimer une personne ------")
          print("1, Retour en Arriere")
          print() 
          nom_personne = input("Saisissez le nom de la personne a modifier: ")
          if(nom_personne == ""):
              print()
              print("Vous ne devez pas laisser le champ vide")
              print()
          elif(nom_personne == "1"):
              break
          elif(nom_personne not in Base_Donnes):
              print()
              print("La Personne n'exite pas, saisissez le nom d'une personne qui existe")
              print()

          else:
            
            del Base_Donnes[nom_personne]

            for elem in Base_Donnes:
                Donnees.append(Base_Donnes[elem])
    
            with open (fichier_csv, "w", newline="") as csv_file:
                csv_reader = csv.DictWriter(csv_file, fieldnames = header)
                csv_reader.writeheader()
                csv_reader.writerows(Donnees)
                print()
                print("Personne suprimée avec SUCCES")
                break

    return



# Menu ==================================
def afficher_menu():
    print()
    print("------ MENU PRINCIPAL PROG CSV ------")
    print("1, Afficher la liste de toutes les personnes enregistrées")
    print("2, Ajouter une nouvelle personne")
    print("3, Modifier les informations d'une personne")
    print("4, Supprimer une personne")
    print("5, Quitter")
    print()



#==============================================================
