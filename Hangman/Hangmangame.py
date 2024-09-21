import random
from hangman_visuals import lives_visual_dict

#def take_word():
Word_Array = ["Car","cat","Wallet","Cash","Fish","Money","Star","Rich"]
s=random.choice(Word_Array)
s=s.lower()
len_s = len(s)
word=[]
cntr=1
list_s = list(s)
hangman_figure_cntr = 0

for i in range(0,len(s)):
    word.append("_")


print(s)
print("You have 7 chances to guess the word")
while cntr <= 7:
    uinp=input("Enter a letter : ")
   # for i in range(0,len(word)): # word has same number of dashes as string
    if uinp in s:
        index_s = list_s.index(uinp)
        word[index_s]=uinp
        print(word)
        final_word = ''.join(word)
        if final_word == s:
            print("you fucking won chhoti")
            break
    else:
        hangman_figure_cntr += 1
        print(lives_visual_dict[hangman_figure_cntr])
        print(word)
    cntr+=1

#take_word()