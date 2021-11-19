"""
Author: Alisha Tiller, abtiller@purdue.edu
Assignment: 12.1 - Solo Wof
Date: 11/17/2021

Description:
    Describe your program here.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import random

def spin_the_wheel():
    
    virtual_wheel = [500,500,500,500,550,550,600,600,600,600,650,650,650,700,700,800,800,900,2500,'BANKRUPT','BANKRUPT']
    # returns at random a value from the virtual wheel that contains the 21 spaces
    cash_values = random.choice(virtual_wheel)
    # cash values are returned as numbers and 'BANKRUPT' is returned as a string
    return cash_values

def load_phrases():
    phrase_list = []
    with open('phrases.txt', 'r') as phrases:
        lines = phrases.readlines()
        # for each line in the file, add that phrase to the phrase_list
        for line in lines: 
            phrase_for_game = line.replace('\n', '')
            phrase_list.append(phrase_for_game)
        # loads all the phrases in the text file and returns them as a list in random order
        phrases = random.choice(phrase_list)

    return phrases

def main():


    phrases = load_phrases()
    round = 0
    index_of_phrase_list = 0 

    for round in phrases:
        round +=1 
        # start with the first phrase in the list (index 0) for round 1
        phrase = phrases[index_of_phrase_list]
        # index increases by one, so each subsequent round of the game uses the next phrase in the list
        index_of_phrase_list += 1


    print(f'Welcome to Solo Wheel of Fortune!')
    print(f'\n \n :: Solo WoF :::::::::::::::::::::::::::::: Round {round} of 4 ::')
    print(f'::     ::')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(f'::   AEIOU   ::   BCDFGHJKLMNPQRSTVWXYZ   ::         $0 ::')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print('\n \n Menu:')
    print('  1 - Spin the wheel.')
    print('  2 - Buy a vowel.')
    print('  3 - Solve the puzzle.')
    print('  4 - Quit the game.\n \n')
    
    player_chooses = input('Enter the number of your choice: ')
    
    menu_dict = {1: 'Spin the Wheel.', 2: 'Buy a vowel.', 3: 'Solve the puzzle.', 4: 'Quit the game.'}
    # using the player_chooses as the key to access the dictionary which contains the value of what acitvity to do
    activity_choosen = menu_dict[player_chooses]
    consonants_to_choose = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    # Spin the Wheel
    consonants_used = []
    # if the player chooses to spin the wheel
    if activity_choosen == 'Spin the Wheel.':
        # the program makes sure that are consonants left to choose by seeing if the list is empty or not
        while consonants_to_choose != []:
            # call the spin_the_wheel function which returns a value at random from a virtual wheel
            cash_value = spin_the_wheel()
            # if bankrupt choosem the player's cash earnings for the round are set to zero and the turn ends
            if cash_value == 'BANKRUPT':
                roung_earnings = 0
            # if the follar amount is chosen
            else: 
                # player is asked to choose a consonant from the list of unused consonants
                player_choice = input('Pick a consonant: ')
                # this makes it so the player choosing a consonant is not case sensitive because it gets converted to a capital
                # letter regardless if the player entered the letter in lowercase or uppercase
                player_choice = player_choice.capitalize()
                # check to see if the letter the player chose is in the list
                if player_choice in consonants_to_choose:
                        # if the player's letter is in the phrase that was selected from the txt file
                        if player_choice in phrase:
                            # count the number of times that letter appears in the phrase 
                            occurrences_of_letter = phrase.count(f'{player_choice}')
                            # player earns the dollar amount of the spin mulitplied by the number of times the guessed letter appears 
                            # in the phrase
                            dollar_amount_earned = cash_value * occurrences_of_letter
                            print(f'There is {occurrences_of_letter}{player_choice}, which earns you ${dollar_amount_earned}.')
                        # remove the consonant from the consonants_to_choose list and add it to the consonants_used list
                        used_consonant = consonants_to_choose.pop(player_choice)
                        consonants_used.append(used_consonant)
                # check to see if the player choose a letter that already has been used from the list of consonants_used 
                elif player_choice in consonants_used:
                    print(f'The letter {player_choice.upper()} has already been used.')
                # check to see if the player enters a number 
                elif player_choice == int(player_choice):
                    print(f'The character {player_choice} is not a letter.')
                # check to see if what the player entered is a string of characters
                elif len(list(player_choice)) > 1: 
                    print(f'Please enter exactly one character.')


    # Buy A Vowel:

    # player's current amount of cash
    player_current_money = 300
    vowels = ['A','E','I','O','U']
    vowels_purchased = []
    if activity_choosen == 'Buy a vowel.':
        if vowels != []:
        # if vowel in vowels:
            # check to see if the player has enough cash in the current round
            if player_current_money > 275:
                vowel_choosen = input('Pick a vowel: ')
                # to make input not case sensitive
                vowel_choosen = vowel_choosen.upper()
                # if the player's letter is in the phrase that was selected from the txt file
                if vowel_choosen in phrase:
                    # count the number of times that vowel appears in the phrase 
                    occurrences_of_vowel = phrase.count(f'{vowel_choosen}')
                    # all occurences of the guessed letter are reveraled and the player's earnings for the round are reduced by $275
                    player_current_money = player_current_money - 275
                    print(f"There is {occurrences_of_vowel} {vowel_choosen}'s.")
                    # to remove the vowel just used and add it to a used list 
                    vowels_bought = vowels.pop(vowel_choosen)
                    vowels_purchased.append(vowels_bought)
                # check if the users vowel pick is in the used list 
                elif vowel_choosen in vowels_purchased:
                    print(f'The letter {vowel_choosen} has already been purchased.')
                # if the users vowel pick is in the consonants list 
                elif vowel_choosen in consonants_to_choose:
                    print(f'Consonants cannot be purchased.')
                # if the users vowel pick length is more than 1
                elif len(list(vowel_choosen)) > 1:
                    print(f'Please enter exactly one character.')
                # if the user vowel pick is not in the phrase selected from the txt file 
                elif vowel_choosen not in phrase:
                    print(f"I'm sorry, there are no {vowel_choosen}'s.")
                # if fails all if statements then, assume it is a symbol character and display the following 
                else:
                    print(f'The character {vowel_choosen} is not a letter.')



    if activity_choosen == 'Solve the puzzle.':
        print('Enter your solution.')
        print(f'Clues:')
        guess = input('Guess: ')
        if guess == phrase:
            print('Ladies and gentlemen, we have a winner! \n')
            print(f'You earned $ this round.')
            #round += 1
        else:
            print("I'm sorry. The correct solution was:")
            print(f'{phrase}')

    if activity_choosen not in menu_dict:
        print(f'"{player_chooses}" is and invalid choice." ')

    if activity_choosen == 'Quit the game.':
        print('\n You earned $0 this round. \n Thanks for playing! \n')
        print('You earned a total of $.')
        


    
                
    

if __name__ == '__main__':
    main()
