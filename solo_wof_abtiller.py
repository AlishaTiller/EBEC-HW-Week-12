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

def main():
    # for loop to iterate 4 times because there are 4 rounds
    #for round in range(4):

    
    phrase_list = []
    with open('phrases.txt', 'r') as phrases:
        lines = phrases.readlines()
        # for each line in the file, add that phrase to the phrase_list
        for line in lines: 
            phrase_for_game = line.replace('\n', '')
            phrase_list.append(phrase_for_game)
        
        phrase = random.choice(phrase_list)

    
    player_chooses = input('Enter the number of your choice: ')
    menu_dict = {1: 'Spin the Wheel.', 2: 'Buy a vowel.', 3: 'Solve the puzzle.', 4: 'Quit the game.'}
    # using the player_chooses as the key to access the dictionary which contains the value of what acitvity to do
    activity_choosen = menu_dict[player_chooses]
    consonants_to_choose = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    consonants_used = []
    # if the player chooses to spin the wheel
    if activity_choosen == 'Spin the Wheel.':
        # the program makes sure that are consonants left to choose by seeing if the dictionary is empty or not
        while consonants_to_choose != {}:
            # call the spin_the_wheel function which returns a value at random from a virtual wheel
            cash_value = spin_the_wheel()
            # if bankrupt choosem the player's cash earnings for the round are set to zero and the turn ends
            if cash_value == 'BANKRUPT':
                roung_earnings = 0
                break
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

                    
                
                
    

if __name__ == '__main__':
    main()
