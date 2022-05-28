#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:33:33 2022

@author: Claudius Odeyemi
"""
'''This code was written with Spyder IDE'''
# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


#Define a function to read the file
def read_file_content(filename):
    with open(filename) as f:
        text=f.read()
    return text

#Define a function to count the words
def count_words():
    text = read_file_content("./story.txt")
    print(text)
    #translate words by removing special characters
    translate = text.maketrans({char: None for char in "'.,:*!"})
    #split clean words
    cleaned_words = text.lower().translate(translate).split()
    #Create a dictionary for our word distribution
    word_counter = {}
    for word in cleaned_words:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    return word_counter

count_words()


