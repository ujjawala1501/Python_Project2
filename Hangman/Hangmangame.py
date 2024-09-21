

import random

Word_Array = ["Car","cat","Wallet","Cash","Fish","Money","Star","Rich"]
s=random.choice(Word_Array)
s=s.lower()
len_s = len(s)
word=[]
cntr=8
 
for i in range(0,len(s)):
    word.append("_")

while cntr > 8:
    uinp=input("Enter a word : ")
    for i in range(0,len(word)): # word has same number of dashes as string 
        if uinp==s[i]:
            word[i]=uinp
        else:
            pass
    print(word)
    cntr-=1

        