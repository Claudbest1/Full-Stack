#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:18:41 2022

@author: macbookpro
"""

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks, score):
        self.name=name
        self.age=age
        self.tracks=tracks
        self.score=score
    #Method 1
    def change_name(self, new_name):
        self.name= new_name
        print( "My name is "+ self.name)
    #Method 2    
    def change_age(self, new_age):
        self.age= new_age
        print( "My age is "+ str(self.age)) 
    #Method 3    
    def add_track(self, new_track):
        self.tracks.append(new_track)
        str1=",".join(self.tracks)
        print( "My track is "+ str1)
     #Method 4    
    def get_score (self):
        print("Your score is "+ str(self.score))
        return self.score
        # print("Your Score is ")+ str(self.score)
      
        
Bob = Student(name=input("Please enter your name: "), age=int(input("Enter your age: ")), tracks=["FE", "BE"], score=float(input("Enter Score: ")))

# Expected methods
Bob.change_name("Peter")
Bob.change_age(28)
Bob.add_track("UI/UX")
Bob.get_score()