def hangman(string):
	sofar = len(string)*["_"]
	print(sofar)
	i = 0
	guess = input('Guess a letter')
	while i < len(string):
		if string[i] == guess:
			print("Got one")
			sofar[i] = guess
			print(sofar)
			guess = input('Guess again')

		i = i + 1


hangman("hello")
