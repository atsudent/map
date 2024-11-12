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

def afiseaza_max():
  max = 0
  for i in elemente:
    if (i > max):
      max = i
  
  print("Max ", max)
  
afiseaza_max()
