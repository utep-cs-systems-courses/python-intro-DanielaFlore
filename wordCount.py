# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:03:21 2020

@author: Flores Daniela
"""

'''
#gathers arguments
import sys
inputFile = sys.argv[1] 
output = sys.argv[2]

f = open(inputFile, "r") 
'''
f = open(r"C:\...\speech.txt", "r")
#stores set of words in speech.txt
dictionary = []
#stores number of times dictionary words are used
counter =[]
bareText = []
sortedDict = []
#iterate through file
for line in f:
    line = line.strip()
    line = line.replace(",","")
    line = line.replace(";","")
    line = line.replace(".","")
    line = line.replace("-","")
    line = line.replace(":","")
    line = line.replace("?","")
    line = line.replace("!","")
    #goes word for word in file
    for word in line.split():
        #store text with no punctuation in list
        bareText.append(word)
        if word in dictionary:
            i = dictionary.index(word)
            continue
        
        elif word not in dictionary:
            dictionary.append(word)
            counter.append(0)

#sorts dictionary alphabetically
sortedDict = sorted(dictionary)
#counts number of times words appear
for word in bareText:
    i = sortedDict.index(word)
    counter[i] = counter[i] +1;

for i in range(len(sortedDict)):
    print(sortedDict[i] , counter[i])

#creates output file and writes solution    
outF = open("output.txt", "w")
for i in range(len(sortedDict)):
  # write line to output file
  outF.write(sortedDict[i])
  outF.write(" ")
  outF.write(str(counter[i]))
  outF.write("\n")
outF.close()
    
    



