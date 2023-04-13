a = "My jesteśmy krasnoludki, hopsasa, hopsasa"
l = a.find("j")
b = a[l:l+8]
print("b ma wartość: " + b)

c = a[-7:]
print("zmienna c ma wartość: " + c)

d = "my"
e = "KRASNOLUDKI"

e = e.lower()
print(e)

d = d.capitalize()
print(d)

print(d + " " + b + " " + e + ", " + c + ", "+ c)


I = "Rwdogrbnrimlnvsspponbnf"
N = "gClkjrvrtudrusjfdoveseh"
Wi = (I[::3])
Wn = (N[1::4])
print(Wi + " " + Wn)


print("liczba liter s: " + str(a.count("s")))
print("liczba liter a: " + str(a.count("a")))


p = "Pxrxogxxrxamxoxwaxnixxexx xtxo xcxzexxscx ixnfxoxxrxxmxaxtxyxkxxixxx."
p = p.replace("x", "")
print(p)


u = float(input("Podaj jakąś liczbę: "))
o = float(input("Podaj drugą liczbę: "))
S = u + o
R = abs(u - o)
P = u**3
m = o**3
r = o%u
M = u%o
print("Suma tych liczb wynosi: " + str(S))
print("1. liczba minus 2. liczba to " + str(R))
print("Potęga 1. liczby to: " + str(P))
print("Potęga 2. liczby to: " + str(m))
print("reszta z dzielenia 2. liczby przez 1. to: " + str(r))
print("reszta z dzielenia 1. liczby przez 2. to: " + str(M))


A = "\033[1;33;46m"
B = "\033[1;30;41m"
C = "\033[1;31;44m"
re = "\033[0m"

print(C + "Programowanie" + re, A + "jest" + re, B + "SUPER" + re)

G = input("Podaj pojedynczą liczbę rzymską: ")
g = input("Podaj drugą pojedynczą liczbę rzymską: ")

if