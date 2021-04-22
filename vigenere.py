
alphabets_lower = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"  # this is the ukrainian letters
alphabets_upper="АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"


def encrypt(p, k):
    c = ""
    kpos = [] # return the index of characters ex: if k='в' then kpos= 2
    for x in k:
        if x.isupper():
            kpos.append(alphabets_upper.find(x))
        else:
            kpos.append(alphabets_lower.find(x))
    i = 0
    for x in p:
      if i == len(kpos):
          i = 0
      if x.isupper():
          pos = alphabets_upper.find(x) + kpos[i]
          #print(pos)
          if pos > 33:
              pos = pos-33               # check you exceed the limit
          c += alphabets_upper[pos]
          i +=1
      else:
          pos = alphabets_lower.find(x) + kpos[i]
          #print(pos)
          if pos > 32:
              pos = pos - 33  # check you exceed the limit
          c += alphabets_lower[pos]
          i += 1
    return c

def decrypt(c, k):
    p = ""
    kpos = []
    for x in k:
        if x.isupper():
            kpos.append(alphabets_upper.find(x))
        else:
            kpos.append(alphabets_lower.find(x))
    i = 0
    for x in c:
      if i == len(kpos):
          i = 0
      if x.isupper():
          pos = alphabets_upper.find(x) - kpos[i]
          if pos < 0:
              pos = pos + 33
          p += alphabets_upper[pos]
          i +=1
      else:
          pos = alphabets_lower.find(x) - kpos[i]
          if pos < 0:
              pos = pos + 33
          p += alphabets_lower[pos]
          i += 1
    return p
try:
    print("Press 1 to Encrypt a message \npress 2 to Decrypt a message")
    choose = input("Choice: ")
    if choose == '1':
       p = input("Enter the plain text: ")
       p = p.replace(" ", "")  # this will make sure that there is no space in the message
       if p.isalpha():
           k = input("Enter the key: ")
           k = k.strip()  # remove the white spaces from both sides
           if k.isalpha():
               c = encrypt(p, k)
               print("The cipher text is: ", c)
           else:
               print(k)
               print("Enter valid key, key is only one character word!")
       else:
           print("Only letters are allowed !!")

    elif choose == '2':
        c = input("Enter the cipher text: ")
        c = c.replace(" ", "")
        if c.isalpha():
            k = input("Enter the key: ")
            if not k.isalpha():
                print("Enter valid key, key is only one character word!")
            else:
                p = decrypt(c, k)
                print("The plain text is: ", p)
        else:
            print("Only letters are allowed!")
    else:
        print("Please enter a valid choice!")
except Exception as e:
    print(e)
    exit("Enter a valid text please! ")