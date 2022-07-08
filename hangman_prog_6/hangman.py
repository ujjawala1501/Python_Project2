import random
from words import words
import string

def get_valid_word(words):
	word = random.choice(words) #randomly chooses something from the list

	while '-' in word or ' ' in word:
		word = random.choice(words)

	return word

def hangman():
	word = get_valid_word(words)
	word_letters = set(word) #letters in the word already guessed -will collect words and store in set-sets, unlike lists or tuples, cannot have multiple occurrences of the same element and store unordered values
	alphabet = set(string.ascii_uppercase) #ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change 
	used_letters = set() # what the user has guessed

	lives = 6
	#USER INPUT
	while len(word_letters) > 0 and lives > 0 :

			#letters used
		print('Your have', live,'lives left and You have used these letters: ', ' '.join(used_letters))
		
		#What current word is (i.e W - R D)
		word_list = [letter if letter in used_letters else '-' for letter in word] # one line loop with list comprehension ha sbeen used here
		print('Current word: ',' '.join(word_list))

		user_letter = input('Guess a letter').upper()
		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)

			else:
				lives = lives-1 # takes away a life if wrong
				print('letter is not in word')

		elif user_letter in used_letters:
			print("you already used that character . Please try again. ")

		else:
			print("invalid character. Please try again...")

    #gets here when len(word_letters) ==0 OR when  lives == 0 
    if lives==0:
 	   print('You died,sorry.The word was',word)
	else:
		print('You guessed the word',word,'!!') 	   

hangman() #calling the function if this wont be here it wont run in cmd

