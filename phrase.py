from character import Character
import random
class Phrase:
    the_answers = ['Carly']#, 'David', 'Sarina', 'Playstation', 'Android', 'Anime', 'Cash', 'Music' ]
    def __init__(self, phrase):
        self.phrase = phrase
        
    def secret_phrase(self):
        random_word = random.choice(self.the_answers)
        phrase_ghost = len(random_word) * ['_']
        
        
        #i did store player_data into a list self.phrase
        #each time i try to compare the 'self.the_answers' with 'self.phrase'
        #it would not work therefore what ever 'if' statement i set would not pass
        #how do i make it work and how would i replace the '_' within phrase_ghost with a letter from self.phrase
        #any ideas? i tried so many things...
        #also this is not finished i will polish this all up in game.py
        #and loop everything to make the game playable 
        
            
                               
player_phrase = []
player_data = input('Please enter a letter: ')
user_characters = Character(player_data)



if len(player_data) == 1:
    print(user_characters.guess_letter())
    print(user_characters.reveal_letter())
    player_phrase.append(player_data)
        
else:
    print('\nPlease enter one letter at a time\n')
        
        
        
the_phrase = Phrase(player_phrase)

print(the_phrase.secret_phrase())