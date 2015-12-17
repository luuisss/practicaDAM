"""3. Algorisme que llegeix dos nombres i mostra com a resultat quin és el més gran"""

A = input("introdueixi un numero: ")
A = int(A)
B = input("introdueixi un numero: ")
B = int(B)
if A > B:
    print("el numero més gran és: ", A)
elif B > A:
    print("el numero més gran és: ", B)

