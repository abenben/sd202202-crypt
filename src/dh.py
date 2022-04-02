"""DH鍵共有"""
import secrets

p = 65537
g = 3
a = secrets.randbelow(p)
b = secrets.randbelow(p)
print("a =", a)
print("b =", b)
A = pow(g, a, p)
B = pow(g, b, p)
print("A =", A)
print("B =", B)
s1 = pow(B, a, p)
s2 = pow(A, b, p)
print("s1 =", s1)
print("s2 =", s2)
