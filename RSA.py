import sys


def findGCD(x, y):
    while y != 0:
        c = x % y
        x = y
        y = c
    return x


def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def coprimes(number):
    l = []
    for x in range(2, number):
        if findGCD(number, x) == 1 and modinv(x, phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x, phi):
            l.remove(x)
    return l


def mod(x, y):
    if (x < y):
        return y
    else:
        c = x % y
        return c


def encryptString(plainText):
    cipher = ""
    for x in list(plainText):
        c = mod(ord(x) ** e, n)
        cipher += (chr(c))
    return cipher


def decryptString(plainText):
    plain = ""
    for x in list(plainText):
        c = mod(ord(x) ** d, n)
        plain += (chr(c))
    return plain


def encryptDecimal(plainText):
    decimalList = plainText.split(" ")
    cipherDecimal = []
    for i in decimalList:
        cipherElement = mod(int(i) ** e, n)
        cipherDecimal.append(cipherElement)
    return cipherDecimal


def decryptDecimal(plainText):
    plainDecimal = []
    for i in plainText:
        cipherElement = mod(int(i) ** d, n)
        plainDecimal.append(cipherElement)
    return plainDecimal


def naturalNumbers():
    i = 1
    while i <= 100:
        f = True
        j = 2
        while f and j < i:
            if not i % j: f = False
            j += 1
        if f: print(i, end=' ')
        i += 1


print("p, q is natural numbers. Like this:")
naturalNumbers()

p = int(input("\nEnter p : "))
q = int(input("Enter q : "))
n = p * q
phi = (p - 1) * (q - 1)

print("\nChoose an coprime from array:")
print(str(coprimes(phi)))

e = int(input("Enter coprime: "))
d = modinv(e, phi)

print("\nPublic key: {e=" + str(e) + ", n=" + str(n) + "}.")
print("Private key: {d=" + str(d) + ", n=" + str(n) + "}.\n")

choice = int(input("What do you want to encrypt?\n 1 - text \n 2 - decimal \nYour choose: "))

if choice == 1:  # text
    s = input("\nEnter a text to encrypt: \n")
    enc = encryptString(s)
    print("\nEncrypted message: " + str(enc) + "\n")
    dec = decryptString(enc)
    print("Decrypted message: " + dec + "\n")
elif choice == 2:  # decimal
    s = input("Enter a hexadecimal numbers to encrypt: ")
    enc = encryptDecimal(s)
    print("\nEncrypted message: ", (str(enc)))
    dec = decryptDecimal(enc)
    print("Decrypted message: ", (str(dec)))
else:
    print("Invalid choice")
