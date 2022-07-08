import random
#guess = 0  
def computer_guess(x):
	low =1
	high =x
	feedback = ''
	guess = 0 
	while feedback != 'c':
	 #giving this condition cause random.randint will throw error if low and high are same
		if low != high:
			guess = random.randint(low,high)
		else:
			guess = low  #could also be high because low=high
		feedback = input(f'Is {guess} too high (H),too low(L),or correct (C)??').lower()
		if feedback == 'h':
			high = guess-1
		elif feedback == 'l':
			low = guess + 1


	print(f"guessed correct {guess}!!")


computer_guess(20)

