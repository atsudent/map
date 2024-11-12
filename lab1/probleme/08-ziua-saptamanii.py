def afiseaza():
  numar_zi = int(input("Introdu ziua"))
  if numar_zi < 1 or numar_zi > 7:
    print("Numar zi invalid. Incearca din nou")
    afiseaza()
    return

  nume_zile = [
    "Luni",
    "Marti",
    "Miercuri",
    "Joi",
    "Vineri",
    "Sambata",
    "Duminica",
  ]
  
  
  print("Ziua sapatamanii cu numarul %d este %s" % (numar_zi, nume_zile[numar_zi - 1]))

afiseaza()
