import random

def processGuess(theAnswer, theGuess):
  position = 0
  clue = ""
  for letter in theGuess:
    if letter == theAnswer[position]:
      clue += "G"
    elif letter in theAnswer:
      clue += "Y"
    else:
      clue += "-"
    position += 1
  print(clue)

#load words and store them in a list
word_list = []
word_file = open("words.txt")
for word in word_file:
  word_list.append(word.strip())

#pick a word
answer = random.choice(word_list)

num_of_guesses = 0
guessed_correctly = False

while num_of_guesses < 6 and not guessed_correctly:
  #get guess from the user
  guess = input("Input your five letter word and press enter:")
  print("You have guessed", guess)
  num_of_guesses += 1

  #process guess
  guessed_correctly = processGuess(answer, guess)

  #display end of game message
  if guessed_correctly:
    print("Congrats! You guessed the correct word in", num_of_guesses, "times")
while num_of_guesses == 6 and not guessed_correctly:
  print("Sorry, You've lost all your guesses. Better Luck Next Time.")
  break