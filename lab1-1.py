import math

R = int(input("Write R: "))
L = int(input("Write L: "))

def calculate (R, L):
    cylinder_volume = math.pi * L * R * R
    return ("cylinder_volume: " + str(cylinder_volume))

print(calculate(R,L))
