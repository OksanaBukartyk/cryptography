from sys import argv


C="lqiobijuvqdoafhusqhfqjxyqddqjyedqbkdyluhiyjo" #зашифрована строка
print("String C = ", C)

if len(C) == 1:
    print("Usage : %s <caesar>" % (__file__))
    exit(1)

key = 'abcdefghijklmnopqrstuvwxyz'
KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            if l.isupper():
                index = KEY.index(l)
                i = (index + n) % 26
                result += KEY[i]
            else:
                index = key.index(l)
                i = (index + n) % 26
                result += key[i]

        except ValueError:
            result += l

    return result

print("№\tVariants")
for n in range(len(C)):
    dec = decrypt(n, C)
    print("%d. %s" % (n, dec))