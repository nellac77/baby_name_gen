# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:02:23 2017

@author: calle
"""
import string
#print(help(string))
print(string.ascii_letters)
print(string.ascii_lowercase)

# I want random selection so I need...
import random

print(random.choice('pull a letter from here'))
print(random.choice(string.ascii_lowercase))
