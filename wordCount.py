# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:03:21 2020

@author: Flores Daniela
"""
'''
TODO: get input file through intrctv mode
'''

f = open(r"C:\...\speech.txt", "r")
#stores set of words in speech.txt
dictionary = []
#stores number of times dictionary words are used
counter =[]
bareText = []
#variables I used to make sure my program isnt skipping any words on file
count = 0
counterTwo = 0
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
        bareText.append(word)
        #keeps track on total amount of words
        count = count + 1
        if word in dictionary:
            i = dictionary.index(word)
            #counter[i] +=1
            continue
        elif word not in dictionary:
            counterTwo = counterTwo + 1
            dictionary.append(word)
            counter.append(1)
sortedDict = sorted(dictionary)

for word in bareText:
    i = sortedDict.index(word)
    counter[i] +=1

for i in range(len(dictionary)):
    print(dictionary[i] , counter[i])


    
outF = open("output.txt", "w")
for i in range(len(sortedDict)):
  # write line to output file
  outF.write(sortedDict[i])
  outF.write(" ")
  outF.write(str(counter[i]))
  outF.write("\n")
outF.close()
    
    


