from math import sqrt

try:
    for a in range(1, 1000):
        for b in range(1, 1000 - a):
            c = (1000 - a - b) 
            if c == sqrt(a**2 + b**2):
                print a*b*c
                raise StopIteration
except StopIteration:
    pass
            
