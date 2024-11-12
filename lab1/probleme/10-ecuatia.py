import math

def rezolva_ecuatia(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2*a)
        return (x, x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x1, x2)
      
print("Rezolva ecuatia: ", rezolva_ecuatia(2, 32 ,8))
