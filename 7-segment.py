#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:23:08 2019

This script will parse a list of words in the dictionary "dictionary.txt"
and determine the longest word(s) that can be displayed on a 
seven-segment display.

Inspired by Tom Scott's video: https://www.youtube.com/watch?v=zp4BMR88260

@author: wes
"""
#convert text file of words to list
f = open('dictionary.txt', 'r')
words = f.readlines()
f.close()

#Letters that cannot be displayed well on a seven-segment display
badletters = 'gkmqvwxz'

#Remove non-displayable words from the list (Slow step)
for word in words:
    if any(elem in word for elem in badletters):
        words.remove(word)
        
#Sort the list by length
sorted_words = sorted(words, key=len)        

#Get the length of the longest word
longest_length = len(sorted_words[len(sorted_words)-1])  

#Print out the words that are >= longest_length
for word in sorted_words:
    if len(word) >= longest_length:
        print(word)    
        print("Length: " + str(longest_length))