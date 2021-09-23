# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:48:42 2021

@author: M BUE
"""

import math


def facteurs(n):
    """facteurs(n): décomposition d'un nombre entier n en facteurs premiers"""
    F = []
    if n==1:
        return F
    # recherche de tous les facteurs 2 s'il y en a
    while n>=2:
        x,r = divmod(n,2)
        if r!=0:
            break
        F.append(2)
        n = x
    # recherche des facteurs 1er >2
    i=3
    rn = math.sqrt(n)+1
    while i<=n:
        if i>rn:
            F.append(n)
            break
        x,r = divmod(n,i)
        if r==0:
            F.append(i)
            n=x
            rn = math.sqrt(n)+1
        else:
            i += 2
    return F



#two prime numbers
p = int(input("p:"))
q = int(input("q:"))


#n = p*q
n = 391
print("n = " + str(n))

phi = (p-1)*(q-1)

print("phi = " + str(phi))
 
# Choose e -> 1 < e < phi 

while(len(facteurs(phi+1))==1 or facteurs(phi+1)[-1]==(phi+1)/ facteurs(phi+1)[-1]):
   phi=phi*2
 
e = facteurs(phi+1)[-1]

#d = int((phi+1)/e)
d = 235
print("e=" + str(e) + " d= " + str(d))

msg = "bonjour"
print("message = " + msg)
print("=======================")
print("public key : (" + str(n) + "," + str(e)+") \nprivate key :("+ str(n) + "," + str(d)+")")
print("=======================")
encryptedmsg = [331, 304, 77, 315, 45, 304, 228, 40, 315, 356]

print("Encryption ...")
for letter in msg:
    print(letter, end="")
    ascii = ord(letter)
    encrypted = int(pow(ascii,e)%n)
    encryptedmsg.append(encrypted)

print(" -> " + str(encryptedmsg))
print("Decryption ...")

decryptedmsg = ""
for letter in encryptedmsg:
    decrypted = int(pow(letter,d)%n)
    decryptedmsg = decryptedmsg + chr(int(decrypted))
    

print("Alice sent : " + str(decryptedmsg))



    

    
 