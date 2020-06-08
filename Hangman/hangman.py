import random
from nltk.corpus import words
word_list = words.words()

def getWord():
	word=random.choice(word_list)
	return word.upper()

def play(word):
	wordCompletion="_"*len(word)
	guessed=False
	guessedLetters=[]
	guessedWords=[]
	tries=6
	print("Let's play Hangman!")
	print(displayHangman(tries))
	print(wordCompletion)
	print("\n")
	while not guessed and tries>0:
		guess=input("Please guess a letter or a word").upper()
		if(len(guess)==1 and guess.isalpha()):
			if(guess in guessedLetters):
				print("You have already guessed this letter: ",guess)
			elif(guess not in word):
				print(guess," is not in word.")
				tries-=1
				guessedLetters.append(guess)
			else:
				print("Good Job! ",guess," is in the word.")
				guessedLetters.append(guess)
				wordAsList=list(wordCompletion)
				indices=[i for i, letter in enumerate(word) if letter == guess]
				for index in indices:
					wordAsList[index]=guess
				wordCompletion="".join(wordAsList)
				if("_" not in wordCompletion):
					guessed=True
		elif(len(guess)==len(word) and guess.isalpha()):
			if(guess in guessedWords):
				print("You have already guessed this word: ",guess)
			elif(guess!=word):
				print(guess," is not the word.")
				tries-=1
				guessedWords.append(guess)
			else:
				guessed=True
				wordCompletion=word
		else:
			print("Not a valid guess.")
		print(displayHangman(tries))
		print(wordCompletion)
		print("\n")
	if(guessed):
		print("Congrats! You guessed the word. You win!!")
	else:
		print("Sorry, you ran out of tries. The word was ",word,". Maybe next time!")


def displayHangman(tries):
    stages=[  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
	word=getWord()
	play(word)
	while(input("Play Again? (Y/N)").upper()=='Y'):
		word=getWord()
		play(word)

if __name__=="__main__":
	main()