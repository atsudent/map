def populeaza_lista():
  number_list = []
  n = int(input("Introdu numarul de elemente"))
  
  for i in range(0, n):
    print("introdu elementul pentru pozitia %d" % (i + 1))
    el = int(input())
    number_list.append(el)
  
  return number_list


elemente = populeaza_lista()

def suma():
  sum = 0
  for i in elemente:
    sum += i
  
  return sum
  
def media():
  print("Media: %d" % (suma() / len(elemente)))

print("Suma: %d" % suma())
media()
