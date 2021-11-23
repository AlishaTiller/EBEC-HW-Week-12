"""
Author: Your Name, login@purdue.edu
Assignment: m.n - Assignment Name
Date: MM/DD/YYYY

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

import matplotlib.pyplot as plt

def main():

    # start an empty list for the gas prices
    letters = []
    frequency_of_letter = {}
    with open('Phrases.txt', 'r') as phrases:
        lines = phrases.readlines()
        # for each line in the file, add that value(number) to the avg_gas_price to form a list
        for line in lines: 
            line = line.strip()
            letters.append(line)
            x = "".join(letters)
            x = x.replace('-', ' ')
            x = x.replace("'", ' ')
            x = x.replace(' ', '')
            x = x.upper()
        
        # print(f'{x}')

        for letter in x:
            if letter in frequency_of_letter:
                frequency_of_letter[letter] += 1
            else:
                frequency_of_letter[letter] = 1

        # print(f'{frequency_of_letter}')
    
        alphabet = ['A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
        index = 0
        quantity_of_letter = []
        for z in alphabet:
            occurrences = alphabet[index]
            y = frequency_of_letter[occurrences]
            y = y/915
            quantity_of_letter.append(y)
            index += 1
        
        # print(f'{quantity_of_letter}')
        total = sum(quantity_of_letter)
        # print(f'{total}')

        key = 0 
        x_values = []
        for k in alphabet:
            x_keys = alphabet[key]
            x_values.append(x_keys)
            key += 1

    # details for creating a line graph 
    fig, ax = plt.subplots()
    x = x_values
    y = quantity_of_letter
    ax.bar(x,y)
    ax.set_title('Letter Frequency in Puzzle Phrases')
    ax.set_xlabel('Letter')
    ax.set_ylabel('Letter Apperance Frequency')
    ax.grid()
    ax.set_ylim(0,0.101)
    plt.show()

if __name__ == '__main__':
    main()
