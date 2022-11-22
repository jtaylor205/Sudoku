import sys
from cow import Cow
from heifer_generator import HeiferGenerator
print(sys.argv)

heifer = HeiferGenerator()
if sys.argv(-1):
    print("Cows available: ", end= " ")
    for i in range(heifer.cows):
        print(heifer.cows[i], end= " ")

