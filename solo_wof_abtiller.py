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
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
vowels = ['A', 'E', 'I', 'O', 'U']

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
            phrase_for_game = phrase_for_game
            phrase_list.append(phrase_for_game)
        # loads all the phrases in the text file and returns them as a list in random order
        random.shuffle(phrase_list)

    return phrase_list

def removed_guess(phrase,guessed):

    result = ''
    for letter in phrase:
        if letter in guessed:
            result = result + ' '
        else:
            result = result + letter

    return result

def phrase_guessed(phrase,guessed):
    result = ''
    for letter in phrase:
        if letter in guessed: 
            result = result + letter
        elif letter.isalpha(): 
            result = result + '_'
        else:
            result = result + letter

    return result 

def status_report(round, phrase, guessed, round_earnings):
    print(f'\n:: Solo WoF :::::::::::::::::::::::::::::: Round {round} of 4 ::')
    print(f'::{phrase_guessed(phrase, guessed).center(54)}::')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(f'::   {removed_guess("AEIOU", guessed)}   ::   {removed_guess("BCDFGHJKLMNPQRSTVWXYZ",guessed)}   ::{("$" + "{:,}".format(round_earnings)).rjust(11)} ::')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print('\nMenu:')
    print('  1 - Spin the wheel.')
    print('  2 - Buy a vowel.')
    print('  3 - Solve the puzzle.')
    print('  4 - Quit the game.\n')

def spin_the_wheel_action(phrase, guessed, player_current_money):
    remaining_consonants = list(filter(lambda letter: not letter in guessed, consonants))
    # player is asked to choose a consonant from the list of unused consonants
    # call the spin_the_wheel function which returns a value at random from a virtual wheel
    cash_value = spin_the_wheel()
    # if bankrupt choosem the player's cash earnings for the round are set to zero and the turn ends
    if cash_value == 'BANKRUPT':
        print(f'The wheel landed on BANKRUPT.\nYou lost ${player_current_money:,}!')
        return '', - player_current_money, True
    print(f'The wheel landed on ${cash_value:,}.')
    player_choice = input('Pick a consonant: ')
    # this makes it so the player choosing a consonant is not case sensitive because it gets converted to a capital
    # letter regardless if the player entered the letter in lowercase or uppercase
    player_choice = player_choice.capitalize()
    # check to see if the player enters a number 
    #if player_choice.isspace() == True:
    if player_choice == '':
            print(f'Please enter exactly one character.')
            return '', 0, False
    if not player_choice in consonants and not player_choice in vowels:
        print(f'The character {player_choice} is not a letter.')
        return player_choice, 0, False
    if player_choice in vowels:
        print(f'Vowels must be purchased.')
        return '', 0, False
    if not player_choice in remaining_consonants:
        print(f'The letter {player_choice.upper()} has already been used.')
        return '', 0, False
    # check to see if what the player entered is a string of characters
    if len(player_choice) > 1: 
        print(f'Please enter exactly one character.')
        return '', 0, False
    if not player_choice in phrase:
        print(f"I'm sorry, there are no {player_choice}'s.")
        return player_choice, 0, False
    # count the number of times that letter appears in the phrase 
    occurrences_of_letter = phrase.count(f'{player_choice}')
    dollar_amount_earned = cash_value * occurrences_of_letter
    if occurrences_of_letter > 1:
        print(f"There are {occurrences_of_letter} {player_choice}'s, which earns you ${dollar_amount_earned:,}.")
    else:
        print(f'There is {occurrences_of_letter} {player_choice}, which earns you ${dollar_amount_earned:,}.')
    # remove the consonant from the consonants_to_choose list and add it to the consonants_used list
    return player_choice, dollar_amount_earned, True

                 
def vowel_action(phrase, guessed, player_current_money):
    # Buy A Vowel
    # player's current amount of cash
    remaining_vowels = list(filter(lambda letter: not letter in guessed, vowels))
    if len(remaining_vowels) == 0:
        print('There are no more vowels to buy.')
        return ''
    if player_current_money < 275:
        print('You need at least $275 to buy a vowel.')
        return ''
    vowel_choosen = input('Pick a vowel: ')
    # to make input not case sensitive
    vowel_choosen = vowel_choosen.upper()
    if vowel_choosen in guessed:
        print(f'The letter {vowel_choosen} has already been purchased.')
        return ''
    # if the users vowel pick is in the consonants list 
    if vowel_choosen in consonants:
        print(f'Consonants cannot be purchased.')
        return ''
    # if the users vowel pick length is more than 1
    if len(vowel_choosen) > 1:
        print(f'Please enter exactly one character.')
        return ''
    # if the user vowel pick is not in the phrase selected from the txt file 
    if not vowel_choosen in phrase:
        print(f"I'm sorry, there are no {vowel_choosen}'s.")
        return ''
    if not vowel_choosen in vowels:
        print(f'The character {vowel_choosen} is not a letter.')
        return ''
    # count the number of times that vowel appears in the phrase 
    occurrences_of_vowel = phrase.count(f'{vowel_choosen}')
    # all occurences of the guessed letter are reveraled and the player's earnings for the round are reduced by $275
    player_current_money = player_current_money - 275
    print(f"There is {occurrences_of_vowel} {vowel_choosen}'s.")
    return vowel_choosen         
                

def puzzle_action(phrase, player_current_money):
    print('Enter your solution.')
    print(f'Clues:')
    guess = input('Guess: ')
    if guess == phrase:
        print('Ladies and gentlemen, we have a winner!\n')
        print(f'You earned ${max(player_current_money,1000)} this round.')
        return True
    print("I'm sorry. The correct solution was:")
    print(f'{phrase}')
    return False

def quit_game(player_current_money,earning_per_round):      
    print(f'\nYou earned ${earning_per_round} this round.\n\nThanks for playing!')
    print(f'You earned a total of ${player_current_money}.')
        

def main():
    print(f'Welcome to Solo Wheel of Fortune!')
    phrases = load_phrases()
    total_earnings = 0
    
    for phrase in phrases:
        phrase = phrase.upper()
        round_earnings = 0
        round = 1
        guessed = ''
        while True:
            if round > 4:
                print(f'You earned a total of ${total_earnings}.')
                break
            # index increases by one, so each subsequent round of the game uses the next phrase in the list
            status_report(round, phrase, guessed, round_earnings)
            player_chooses = input('Enter the number of your choice: ')
            # using the player_chooses as the key to access the dictionary which contains the value of what acitvity to do
            if player_chooses == '1':
                guessed_consonant, dollar_amount_earned, next_round = spin_the_wheel_action(phrase, guessed, round_earnings)
                guessed += guessed_consonant
                round_earnings += dollar_amount_earned
                # if next_round:
                #     round += 1 
            elif player_chooses == '2':
                guessed_vowel = vowel_action(phrase, guessed, round_earnings)
                guessed += guessed_vowel
                if guessed_vowel != '':
                    round_earnings -= 275
            elif player_chooses == '3':
                solved = puzzle_action(phrase, round_earnings)
                if solved:
                    total_earnings += round_earnings
                    break 
                else: 
                    round += 1
            elif player_chooses == '4':
                quit_game(total_earnings, round_earnings)
                return
            else: 
                # if activity_choosen not in menu_dict:
                print(f'"{player_chooses}" is an invalid choice." ')

    
        


    
                
    

if __name__ == '__main__':
    main()
