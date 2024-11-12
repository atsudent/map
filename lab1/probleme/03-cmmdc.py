def cmmdc():
  a = int(input("Primul numar: "))
  b = int(input("Al doilea numar: "))
  
  while b != 0:
    a, b = b, a % b
  
  print("Cmmdc %d" % a)
  
cmmdc()
