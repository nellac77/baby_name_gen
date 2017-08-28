# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:08:44 2017

@author: calle
"""

import random, string

# Ask for inputs
letter_1_input = input('Select a letter option: "v" for vowel, "c" for consonant, or "l" for any.')
letter_2_input = input('Select a letter option: "v" for vowel, "c" for consonant, or "l" for any.')
letter_3_input = input('Select a letter option: "v" for vowel, "c" for consonant, or "l" for any.')
letter_4_input = input('Select a letter option: "v" for vowel, "c" for consonant, or "l" for any.')
letter_5_input = input('Select a letter option: "v" for vowel, "c" for consonant, or "l" for any.')

# The options
vowels = 'aeiou'
consonents = 'bcdfghjklmnpqrstvwxyz'
letter = string.ascii_lowercase

# Create our own functions, 5 separate random letters for 5 separate vars
def generator():
    
#    letter1 = random.choice(string.ascii_lowercase)
#    letter2 = random.choice(string.ascii_lowercase)
#    letter3 = random.choice(string.ascii_lowercase)
#    letter4 = random.choice(string.ascii_lowercase)
#    letter5 = random.choice(string.ascii_lowercase)
    
    """ TO DO: The follwoing is bad. I mean, ugly... 
    I was following a guide for practice purposes, but I will be back
    to make this better. I mean, it hurts to look at."""
    # The conditionals
    if letter_1_input == "v":
        letter1 = random.choice(vowels)
    elif letter_1_input == "c":
        letter1 = random.choice(consonents)
    elif letter_1_input == "l":
        letter1 = random.choice(letter)
    else:
        letter1 = letter_1_input # Let's user select SPECIFIC letter
        
    if letter_2_input == "v":
        letter2 = random.choice(vowels)
    elif letter_2_input == "c":
        letter2 = random.choice(consonents)
    elif letter_2_input == "l":
        letter2 = random.choice(letter)
    else:
        letter2 = letter_2_input # Let's user select SPECIFIC letter
        
    if letter_3_input == "v":
        letter3 = random.choice(vowels)
    elif letter_3_input == "c":
        letter3 = random.choice(consonents)
    elif letter_3_input == "l":
        letter3 = random.choice(letter)
    else:
        letter3 = letter_3_input # Let's user select SPECIFIC letter
        
    if letter_4_input == "v":
        letter4 = random.choice(vowels)
    elif letter_4_input == "c":
        letter4 = random.choice(consonents)
    elif letter_4_input == "l":
        letter4 = random.choice(letter)
    else:
        letter4 = letter_4_input # Let's user select SPECIFIC letter
        
    if letter_5_input == "v":
        letter5 = random.choice(vowels)
    elif letter_5_input == "c":
        letter5 = random.choice(consonents)
    elif letter_5_input == "l":
        letter5 = random.choice(letter)
    else:
        letter5 = letter_5_input # Let's user select SPECIFIC letter
    
    # Cough out the name    
    name = letter1 + letter2 + letter3 + letter4 + letter5
    
    # Let the world know
    return name


# Maybe we'll get a hit
for babynames in range(5):        
    print(generator())