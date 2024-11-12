def este_prim(numar):
  if numar <= 1:
    return False
  if numar <= 3:
    return True
  if numar % 2 == 0 or numar % 3 == 0:
    return False
  
  i = 5
  while i * i < numar:
    if numar % i == 0 or numar % (i + 2) == 0:
      return False
    i += 6
  
  return True

numar = int(input("Introdu numarul: "))

print("Este prim %s" % este_prim(numar))