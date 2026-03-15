# somme et moyenne de notes
def calcul_moyenne(notes):
  somme = 0
  for note in notes:
    somme = somme+ note  # on additionne toutes les notes
  
  moyenne = somme / len(notes)  # division par le nombre de notes
  print("La moyenne de cet eleve est:", round(moyenne, 2))
  # Appréciation selon la moyenne
  if moyenne > 16:
    print("Appréciation : Excellent travail, BRAVO ! 🎉")
  elif 11 <= moyenne <= 16:
    print("Appréciation : Bon travail, continue comme ça ! 👍")
  else:  # myenne inferieur a 10
    print("Appréciation : Courage, tu peux t'améliorer, accroche toi ! 💪")

#Tests
calcul_moyenne([5, 7, 9, 8, 6])        # Appréciation : Courage
calcul_moyenne([12, 15, 14, 11, 13])   # Appréciation : Bon travail
calcul_moyenne([18, 17, 19, 20, 16])   # Appréciation : Excellent
