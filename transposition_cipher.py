# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 15:24:36 2019

@author: mpstme.student
"""
## Enter the plain_txt

plain_txt= input("Enter the string to be encrypted: ")

# Enter the key

key= int(input("Enter the key: "))

#Convert plain_txt string to list

plain_txt= list(plain_txt)
cipher_txt=[]
n=len(plain_txt)

#loop to conver plain_txt to cipher txt
for i in range(n):
    temp= plain_txt[(i-key)%n]
    cipher_txt.append(temp)
    
cipher_txt="".join(cipher_txt)
print(cipher_txt)

# loop to convert cipher_txt to plain_txt
cipher_txt= list(cipher_txt)
retrieved_txt=[]
for i in range(n):
    temp1= cipher_txt[(i+key)%n]
    retrieved_txt.append(temp1)
    
retrieved_txt="".join(retrieved_txt)
print(retrieved_txt)