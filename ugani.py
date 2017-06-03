# -*- coding: utf-8 -*-
import random
randomNumber = random.randint(1,100)

print u"Izbral sem si naključno številko med 1 in 100, poskusi jo uganiti. Za izhod iz programa napiši 'exit'."
userGuess = raw_input("Ugibaj: ")

numberOfGuesses = 0

while True:
    
    if (userGuess == "exit"):
        exit()
    
    numberOfGuesses += 1
    
    if (int(userGuess) == randomNumber):
        print u"Pravilno. Potreboval si %s poskusov." % numberOfGuesses
        userInput = raw_input("Ponovi igro? (da/ne)")
        
        if (userInput == "da"):
            randomNumber = random.randint(1,100)
            numberOfGuesses = 0
            print u"Izbral sem si novo številko, poskusi jo uganiti."
            userGuess = raw_input("Ugibaj: ")
            continue
        else:
            break
        
    elif (int(userGuess) > randomNumber):
        print u"Tvoja številka je previsoka."
        userGuess = raw_input("Ugibaj: ")
        
    elif (int(userGuess) < randomNumber):
        print u"Tvoja številka je prenizka."
        userGuess = raw_input("Ugibaj: ")

    