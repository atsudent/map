def populeaza_lista():
  lista_unghiuri = []
  n = 0
  while n < 3:
    print("introdu unghiul nr %d" % (n + 1))
    el = int(input())
    if el <= 0 or el >= 180:
      print("Unghi invalid. Incearca din nou")
      continue
    n += 1
    lista_unghiuri.append(el)
  
  return lista_unghiuri


unghiuri = populeaza_lista()

def suma():
  sum = 0
  for i in unghiuri:
    sum += i
  
  return sum

def unghiuri_valide_pentru_triunghi():
  s = suma()
  if s != 180:
    print("Suma unghiurilor trebuie sa fie 180; avem %d" % s)
  else:
    print("Ok")

unghiuri_valide_pentru_triunghi()
