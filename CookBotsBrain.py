# Process Module
from CookBotsKnowledge import*
from datetime import *
import random
import string

# code inspired by https://www.programiz.com/python-programming/examples/remove-punctuation
def processUserMessage(message):
    '''This function takes a string as an input, returns a string in lower case without punctuation, brackets etc.'''
    punctuation = string.punctuation
    newMessage = ''
    for letter in message:
        if letter not in punctuation:
            newMessage += letter
    return newMessage.lower()
# end of code inspired by https://www.programiz.com/python-programming/examples/remove-punctuation

def separateContractions(wordList):
    '''This function takes a list of strings as an input. Every element containing an apostrophe is replaced
    by two elements, one of them being the contraction and the other one whatever is left. Apostrophe is left only in n't.
    A new list of strings is returned.'''
    newList = wordList.copy()
    for word in wordList:
        if "'" in word:
            position = word.find("'")
            if word[position - 1].lower() == 'n': # for n't contractions
                newList.append(word[0:(position - 1)]) # the part of the word before the contraction
                newList.append(word[(position - 1):]) # the contraction
            else:
                newList.append(word[0:position]) # the part of the word before the contraction
                newList.append(word[position+1:]) # the contraction without apostrophe
            newList.remove(word)
    return newList

def meaningfulWords(message):
    '''This function takes a string as an input and returns a list of meaningful words.'''
    listOfWords = message.split() # create a list because separateContractions takes a list as an input
    listOfWords2 = separateContractions(listOfWords) # "don't" -> "do", "n't"
    strMessage = ' '.join(listOfWords2) # transform to a string again
    processedMessage = processUserMessage(strMessage) # delete punctuation, to lowercase
    processedList = processedMessage.split() # create a list again so we can check each word
    meaningfulList = []
    for word in processedList:
        if word not in uselessWords:
            meaningfulList.append(word)
    return meaningfulList

#x = "I don't like tomatoes."
#y = "I'd like to make a pizza. I am allergic to peanuts"
#z = "I've got an apple. I don't have tomatoes."
#print(meaningfulWords(x))
#print(meaningfulWords(y))
#print(meaningfulWords(z))

#print(processUserMessage("Hola! (vsss)gr JZRFa<sdf: ski'rj."))

def fixedAnswer(message):
    '''This function takes a string as an input and returns a string which an appropriate reply to a given message or
    an empty string if the message is not in the list fixedMessages.'''
    message = processUserMessage(message)
    for i in range(len(fixedMessages)): # for every dictionary in the list of fixed messages
        if message in fixedMessages[i]['message']: # if the message is a value of the key 'message' in the i-th dictionary
            listOfAnswers = fixedMessages[i]['response']
            answer = random.choice(listOfAnswers)
            return answer
    return ''

#print(fixedAnswer('hey'))

def daytimeRecipe(dietList, healthList):
    '''This function takes 2 lists inputs and returns a recipe according to current time. A breakfast recipe before 9 am,
    a lunch recipe before 12 am, a dinner recipe after 12 am.'''
    hourNow = datetime.now().hour
    if hourNow < 9:
        keyword = 'breakfast'
    elif hourNow < 12:
        keyword = 'lunch'
    else:
        keyword = 'dinner'
    recipeList = searchOutput(keyword,healthList,dietList)
    try:
        firstFound = recipeList[0]
    except IndexError:
        return "I am sorry. I couldn't find a recipe for you."
    recipeName = firstFound['label']
    recipeUrl = firstFound['url']
    answer = ("I am sorry. Search for another recipe or try this one: " + recipeName + '\nYou can find the full recipe on ' + recipeUrl)
    return answer

#print(daytimeRecipe())


# x = ["i", "don't", "like", "tomatoes"]
# y = ["i'd", "like","to","make", "a", "pizza"]
# print(separateContractions(x))
# print(separateContractions(y))



def extractDiets(sentence):
    '''This function takes a string as an input and returns a list of diet filters.'''
    sentence = processUserMessage(sentence)
    diets = []
    if 'low' in sentence and 'fat' in sentence or 'lowfat' in sentence:
        diets.append('low-fat')
    if 'low' in sentence and 'carb' in sentence or 'lowcarb' in sentence:
        diets.append('low-carb')
    if 'high' in sentence and 'protein' in sentence or 'highprotein' in sentence:
        diets.append('high-protein')
    if 'balanced' in sentence:
        diets.append('balanced')
    return diets

def extractHealthFilters(sentence):
    '''This function takes a string as an input and returns a list of health filters.'''
    sentence = processUserMessage(sentence)
    health = []
    if 'vegan' in sentence:
        health.append('vegan')
    if 'vegetarian' in sentence:
        health.append('vegetarian')
    condition1 = 'allergic' in sentence or 'allergy' in sentence
    if condition1 and ('peanut' in sentence or 'nut' in sentence):
        health.append('peanut-free')
    if condition1 and ('tree nut' in sentence or 'treenut' in sentence):
        health.append('tree-nut-free')
    if 'alcoholfree' in sentence or 'alcohol free' in sentence:
        health.append('alcohol-free')
    return health


def semiIntelligentAnswer(message, index): # for discord
    '''This function takes 2 inputs: a string and an integer. It returns a string which is a recipe based on the message.
    The index enables to search through the recipes.'''
    sentence = processUserMessage(message)

    # search for diets
    diets = extractDiets(sentence)
    #search for allergies
    health = extractHealthFilters(sentence)
    # delete words related to allergies so that they don't get among keywords
    wordsToDelete = []
    if 'peanut-free' in health:
        wordsToDelete.append('peanut')
        wordsToDelete.append('peanuts')
    if 'tree-nut-free' in health:
        wordsToDelete.append('treenut')
        wordsToDelete.append('tree')
        wordsToDelete.append('nut')
        wordsToDelete.append('nuts')
    if 'alcohol-free' in health:
        wordsToDelete.append('alcohol')

    # extract keywords most likely to be a name of a recipe
    usefulWords = meaningfulWords(message)
    for word in wordsToDelete: # delete words related to diets and allergies from usefulWords
        if word in usefulWords:
            usefulWords.remove(word)

    keywords = ' '.join(usefulWords)
    print(keywords)
    print(diets)
    print(health)
    #print(index)
    recipes = searchOutput(keywords, health, diets)
    if recipes != []:
        try:
            recipe1 = recipes[index]
        except IndexError:
            return "I am sorry. I couldn't find a recipe for you."
        answer = 'You can try ' + recipe1['label'] + '. You only need these ingredients:\n'
        for ingredient in recipe1['ingredientLines']:
            answer = answer + ingredient +'\n'
        answer += 'You can find the full recipe on ' + recipe1['url'] +'\nDo you like it?'
    else:
        answer = daytimeRecipe(diets, health)
    return answer

#semiIntelligentAnswer("I would like some pizza, but i'm vegetarian. And I am allergic to tree nuts.")

def semiIntelligentAnswer1(message): # for terminal
    '''This function takes 2 inputs: a string and an integer. It returns a string which is a recipe based on the message. Additional questions
    are asked if the user did not provide sufficient information.'''
    sentence = processUserMessage(message)
    # search for diets
    diets = extractDiets(sentence)
    #search for allergies
    wordsToDelete = []
    health = extractHealthFilters(sentence)
    # if the user has not mentioned any diets or allergies, ask for them
    if health == []:
        askForAllergy = input('Are you allergic to anything? Would you like to it to be vegan or vegetarian?')
        health = extractHealthFilters(askForAllergy)
    if diets == []:
        askForDiets = input('Are you on any special diet? Like low-fat, high-protein, balanced... ')
        diets = extractDiets(askForDiets)

    # extract keywords most likely to be a name of a recipe
    usefulWords = meaningfulWords(message)
    for word in wordsToDelete:
        if word in usefulWords:
            usefulWords.remove(word)
    keywords = ' '.join(usefulWords)

    recipes = searchOutput(keywords, health, diets)
    if recipes != []:
        recipe1 = recipes[0]
        answer = 'You can try ' + recipe1['label'] + '. You only need these ingredients:\n'
        for ingredient in recipe1['ingredientLines']:
            answer = answer + ingredient +'\n'
        answer += 'You can find the full recipe on ' + recipe1['url']
    else:
        answer = daytimeRecipe(diets, health)
    return answer





