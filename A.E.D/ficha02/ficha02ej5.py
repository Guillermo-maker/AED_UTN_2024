x = (int(input("numero x: ")))
e = (int(input("numero e: ")))

hip = (x**2 + e**2) ** (1/2)

alfa = x/hip
delta = e/hip

print(alfa)
print(delta)