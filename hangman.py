import random

print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']
selected = random.choice(words)
remaining_set = set(selected)
word = set(selected)
guessed_letters = set()
typed_letters = set()

lives = 8
dash = '-'

game = input('Type "play" to play the game, "exit" to quit: ')
if game == 'play':
    run = True
elif game == 'exit':
    run = False
while run and lives > 0:     
    print()
    result = ''.join(letter if letter in guessed_letters else dash for letter in selected)
    print(result)

    new_letter = input("Input a letter: ")
    
    if len(new_letter) != 1:
        print('You should input a single letter')

    elif new_letter.isascii() == False or new_letter.islower() == False:
        print('Please enter a lowercase English letter')

    elif new_letter in remaining_set:
        guessed_letters.add(new_letter)
        remaining_set.discard(new_letter)
        typed_letters.add(new_letter)
        if guessed_letters == word:
            result = ''.join(letter if letter in guessed_letters else dash for letter in selected)
            print()
            print(result)
            break
          
    elif new_letter in typed_letters:
        print("You've already guessed this letter")
        # lives -= 1
            
    elif new_letter not in word:
        typed_letters.add(new_letter)
        print("That letter doesn't appear in the word")
        lives -= 1

if game != 'exit' and lives > 0:
    print("You guessed the word!")
    print("You survived!") 
elif game != 'exit' and lives == 0:        
    print("You lost!")   

# print()
# print("Thanks for playing!")
