import random 

index = -1
gameWords = ("python","java","CSharp","Android") #string tuple

word = random.choice(gameWords) #sets to random string in tuple
word_length = len(word)
guess = ""
attempts = 0
enter = ""
print(word)
hide_letter = "_" * word_length 

print("The word chosen by computer has", word_length,"letters.")
print("Take a guess and see if your letter is in computer word.\n")
print("You will have 8 chances to solve.\n")

for i in range(0, 8):
    attempts +=1
    guess = input("Guess. "+str(attempts)+":") #user input
    if guess in word and guess != enter: #accounts for blank input
        for i in range(0, word_length):
            if guess == word[i]: # check if guess is in word
                hide_letter = hide_letter[:i] + guess +hide_letter[i+1:] #return string of correct guesses and remaining slots
        print("yes\n" + hide_letter)  
    if guess not in word:
        print("no")
    if "_" not in hide_letter:
        print("Good Job, Continue")
        break
    elif attempts == 8: #number of chances met
        guess = input("And the word is:")
        if guess == word:
            print("Great job, thanks for playing")
        else:
            print("Sorry, your word was: " + word)




