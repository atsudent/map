def populeaza_lista():
  number_list = []
  n = 0
  while n < 5:
    print("introdu elementul nr %d" % (n + 1))
    el = int(input())
    n += 1
    number_list.append(el)
  
  return number_list


elemente = populeaza_lista()

def sort_list(lista_numere):
  print("Lista nesortata ", lista_numere)
  n = len(lista_numere)

  for i in range(n):
    for j in range(0, n-i-1):
      if elemente[j] > elemente[j+1]:
        elemente[j], elemente[j+1] = elemente[j+1], elemente[j]
    
  print("Lista sortata ", elemente)
  
sort_list(elemente)