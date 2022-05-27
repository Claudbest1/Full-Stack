#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 10:14:38 2022

@author: macbookpro
"""

# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if sorted(word)==sorted(anagram):
        return True
    else:
        return False
    
word=input("Enter the word: ")
anagram=input("Enter the anagram you which to confirm: ")
find_anagram(word, anagram)