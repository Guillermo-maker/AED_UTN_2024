a = (int(input("numero a: ")))
b = (int(input("numero b: ")))
c = (int(input("numero c: ")))
x = (int(input("numero x: ")))

cuadpol = a*x**2 + b*x + c

ecuara = (-b + (b**2 - 4*a*c)**0.5) / (2*a)

print(ecuara)
print(cuadpol)