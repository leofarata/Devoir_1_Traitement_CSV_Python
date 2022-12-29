from lib.prog_csv import *

# MAIN =================================================
while True:
  afficher_menu()
  choix = input("Votre choix: ")

  if(choix == "1"):
      Afficher_Personnes(fichier_csv)
      
  elif(choix == "2"):
      Ajouter_Nouvelle_Pernonne(fichier_csv)
      
  elif(choix == "3"):
      Modifier_Infos_Personne(fichier_csv)
      
  elif(choix == "4"):          
      Supprimer_Personne(fichier_csv)
      
  elif(choix == "5"):
      break
