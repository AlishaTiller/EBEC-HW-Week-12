"""
Author: Alisha Tiller, abtiller@purdue.edu
Assignment: 12.2 - Wof Analysis
Date: 11/22/2021

Description:
    The program counts the number of times each letter is used from 
    the phrases that could be used in a game of Wheel of Fortune. It 
    then takes this data and creates a bar graph showing the occurrences 
    of each letter relative to the total number of letters in phrase.txt
    file.

Contributors:
    None

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

import matplotlib.pyplot as plt

def main():

    letters = []
    frequency_of_letter = {}
    with open('Phrases.txt', 'r') as phrases:
        lines = phrases.readlines()
        # for each line in the file, delete the space, add to a list
        for line in lines: 
            line = line.strip()
            letters.append(line)
            # turn many strings into one string
            phrases_in_one_str = "".join(letters)
            # replace the following with a space or nothing
            phrases_in_one_str = phrases_in_one_str.replace('-', ' ')
            phrases_in_one_str = phrases_in_one_str.replace("'", ' ')
            phrases_in_one_str = phrases_in_one_str.replace(' ', '')
            phrases_in_one_str = phrases_in_one_str.upper()
        # for each letter in phrases_in_one_string... 
        for letter in phrases_in_one_str:
            # if the letter is in the list frequency_of_letter, add an occurrence to that letter
            if letter in frequency_of_letter:
                frequency_of_letter[letter] += 1
            else:
                frequency_of_letter[letter] = 1
        # x-values/labels for graph and key to access dicitonary
        alphabet = ['A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
        # to create a list of elements for the y-values of the graph
        index = 0
        quantity_of_letter = []
        for single_letter in alphabet:
            # to access each element in a list one at a time for all 26 letters in alphabet
            single_letter = alphabet[index]
            # use the element as the key to access the value in the frequency_of_letter dictionary
            occurrences = frequency_of_letter[single_letter]
            # the number of times each letter is used divided by the total number of letters
            occurrences = occurrences/915
            # add this occurrence value to a new list 
            quantity_of_letter.append(occurrences)
            index += 1
        # totals the number of occurences of each letter from the list (= 915)
        total = sum(quantity_of_letter)
    # details for creating a line graph 
    fig, ax = plt.subplots()
    phrases_in_one_str = alphabet
    occurrences = quantity_of_letter
    ax.bar(phrases_in_one_str,occurrences)
    ax.set_title('Letter Frequency in Puzzle Phrases')
    ax.set_xlabel('Letter')
    ax.set_ylabel('Letter Apperance Frequency')
    ax.grid()
    ax.set_ylim(0,0.101)
    plt.show()

if __name__ == '__main__':
    main()
