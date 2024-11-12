def afisare1():
  n = 0;
  while(n < 20):
    n += 1
    if (n % 2 != 0):
      print("Impar: %d" % n)
      
def afisare2():
  for n in range(0, 20):
    if (n % 2 != 0):
      print("Impar: %d" % n)

afisare1()
afisare2()