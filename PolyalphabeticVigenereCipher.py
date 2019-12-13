#!/usr/bin/env python
# coding: utf-8

# ## Polyalphabetic Cipher- Vigenere Cipher

# In[1]:


## create set of characters for plain text and cipher text

import string
allLetters= string.ascii_letters
digits= "0123456789"
specialAlphabets= " !@#$%^&*"
allLetters= allLetters+digits+specialAlphabets

print("Set of characters: ", allLetters)
## Enter plain text and key 

PT=input("Enter the plain text from the above set of characters: ")
Key= input("Enter the key from the above set of characters: ")


# In[2]:


## develop a key stream
n=len(PT)
m=len(Key)
l=int(n/m)
p= n%m
Key = l*Key+ Key[0:p]

## convert plain text string to list

PT= list(PT)

## find the index of the key corresponding to its character from the set of characters
keyIndex=[]
for k in Key:
    for i in range(len(allLetters)):
        if k==allLetters[i]:
            temp=i
    keyIndex.append(temp)
#print(keyIndex)
    


# In[3]:


# Obtain the cipher text for the given character in the plain text and the corresponding key

CT=[]
z=0
for char in PT:
    for i in range(len(allLetters)):
        if char== allLetters[i]:
            num= (i+keyIndex[z])%len(allLetters)
            temp= allLetters[num]
    CT.append(temp)
    z=z+1
CT="".join(CT)
print("Cipher text is: ",CT)

    


# In[4]:


## Obtain decrypted text from the cipher text and the corresponding key

DT=[]
z=0
for char in CT:
    for i in range(len(allLetters)):
        if char== allLetters[i]:
            num= (i-keyIndex[z])%len(allLetters)
            temp= allLetters[num]
    DT.append(temp)
    z=z+1
DT="".join(DT)
print("Decrypted Text is: ",DT)


# In[ ]:





# In[ ]:




