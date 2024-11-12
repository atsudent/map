def suma1():
  sum = 0
  for i in range(0, 101):
    sum = sum + i
  print("Suma: %d" % sum)

def suma2():
  sum = 100 * (100 + 1) // 2
  print("Suma %d" % sum)

suma1()
suma2()