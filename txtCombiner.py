#Kevin Curtin A1
#thekevincurtin@gmail.com
#I worked on this assignment alone

#This program will take multiple .txt files in a directory
#and combine their contents, resulting in one .txt file with all the contents

#I got the idea because I like to have a seperate .txt file for each week
#when I am taking notes in class, combining them all into one will make studying
#for the final easier as long as there is not a ton of notes

import os
from os.path import *

def txtCombiner(p):
    txtList = []                 #combined text will go in this list
    main = os.listdir(p)
    for item in main:
        path = p + sep + item
        if ".txt" in item:
            f = open(path,"r")
            txtList.append(f.readlines)
            f.close
    print(txtList)

#txtCombiner("C://Users//kevincurtin//Desktop")
