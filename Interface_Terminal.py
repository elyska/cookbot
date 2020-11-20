# Interface Module to run in the terminal
from CookBotsBrain import*
import random

a = "Hello, I am your CookBot. What recipe are you looking for?"
b = "Hello, I am your cookbot, what would you like to eat today?"
c = "Hello, I am your cookbot, what are you craving today?"

testlist = [a, b, c]
print(random.choice(testlist))

while True:
    userMessage = input()
    if userMessage != '':
        sentence = processUserMessage(userMessage)
        inMemory = fixedAnswer(sentence)
        if inMemory != '':
            print(inMemory)
        else:
            print(semiIntelligentAnswer1(userMessage))
        userMessage = ''