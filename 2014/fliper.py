
# metódo simples
'''portas = input().split()

if portas[0] == "0":
    print("C")
elif portas[1]== "0":
    print("B")
else:
    print("A") '''

# Tentátiva mais simples porém mais sagaz

'''portas = input()

if portas == "0 0" or portas == "0 1":
    print("C")
elif portas == "1 0":
    print("B")
else:
    print("A") '''

# Solução após ver o gabarito

P, R = input().split()

if P == "0":
    print("C")
elif R == "0":
    print("B")
else: 
    print("A")