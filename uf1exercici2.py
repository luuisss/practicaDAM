"""2. Algorisme que llegeix un nombre i ens indica si és major que 10 o no."""

A = input("introduei un numero: ")
A = int(A)
if A > 10:
    print("el numero introduit es major de 10")
elif A < 10:
    print("el numero introduit es menor de 10")
else:
    print("el numero es 10")
