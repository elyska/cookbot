# Data Module

import requests
import json
import DummyRecipe

#######################################################################################
############# code from https://www.nltk.org/book/ch02.html ###########################
#######################################################################################

from nltk.corpus import stopwords
#nltk.download('stopwords')
uselessWords = stopwords.words('english')

#######################################################################################
############# end of code from https://www.nltk.org/book/ch02.html ####################
#######################################################################################

addUselessWords = ['would','not','cook','like','have','got','make','allergy','allergic',
                   'lowcarb','diet', 'low', 'carb', 'fat', 'lowfat', 'balanced', 'high',
                   'protein', 'highprotein', 'vegan', 'vegetarian','please','want',
                   'prepare','help','thanks','thank','nt','dont']

uselessWords = uselessWords + addUselessWords

availableDiets = ['balanced', 'high-protein', 'low-fat', 'low-carb']
availableHealthFilters = ['vegan', 'vegetarian', 'peanut-free', 'tree-nut-free',
                          'alcohol-free']

#######################################################################################
################################ code based on ########################################
#https://www.linkedin.com/learning/using-python-for-automation/using-api-keys?u=2039756
############# and https://developer.edamam.com/edamam-docs-recipe-api #################
#######################################################################################

def accessApi(keywords, healthList, dietList):
    '''This function takes 3 inputs: keywords is a string, healthList and dietList are
    lists of strings. It returns the data from API search as a dictionary.'''
    apiUrl = "https://api.edamam.com/search"
    parameters = {'app_id': '14a3021a', 'app_key': 'f89043d78ea9c82982e8b1ae788a04f9',
                  'q':keywords,'health':healthList,'diet':dietList}
    if len(healthList) == 0:
        parameters.pop('health') # delete key from dictionary if it is not needed
    if len(dietList) == 0:
        parameters.pop('diet') # delete keys from dictionary if it is not needed
    response = requests.get(apiUrl, params=parameters)
    searchJson = response.content # data in json format
    #print(type(searchJson))

    # convert searchJson (bytes) to string, necessary for some versions of Python
    # https://docs.python.org/3/howto/unicode.html
    searchJson = searchJson.decode('utf-8')

    output = json.loads(searchJson) # convert json to dictionary
    return output

#######################################################################################
############################ end of code based on #####################################
#https://www.linkedin.com/learning/using-python-for-automation/using-api-keys?u=2039756
############## and https://developer.edamam.com/edamam-docs-recipe-api ################
#######################################################################################

def dummyAccessApi():
    return DummyRecipe.dummyRecipe

def searchOutput(keywords, healthList, dietList):
    '''This function takes 3 inputs: keywords is a string, healthList and dietList are
    lists of strings. It returns only useful data (label, url, dietLabels, healthLabels,
    ingredientLines) for each recipe from API search as a list of dictionaries.'''
    dataFound = accessApi(keywords, healthList, dietList)
    #dataFound = dummyAccessApi()
    hits = dataFound['hits']
    listOfRecipes = []
    for element in hits:
        recipe = {}
        recipe['label'] = element['recipe']['label']
        recipe['url'] = element['recipe']['url']
        recipe['dietLabels'] = element['recipe']['dietLabels']
        recipe['healthLabels'] = element['recipe']['healthLabels']
        recipe['ingredientLines'] = element['recipe']['ingredientLines']
        listOfRecipes.append(recipe)
    return listOfRecipes

fixedMessages = [
    {
        'message': ['thanks', 'thank you', 'thx'],
        'response':['No problem', "You're welcome", "My pleasure"]
    },
    {
        'message': ['hi', 'hello', 'hey', 'good morning', 'good afternoon',
                    'good evening', 'gm'],
        'response':['Hi', 'Hello']
    },
    {
        'message': ['bye', 'goodbye', 'see you later', 'see ya'],
        'response':['Bye', 'Goodbye']
    },
    {
        'message': ['whats your name', 'who are you', 'who am i talking to'],
        'response':['I am CookBot.']
    },
    {
        'message': ['how are you', 'how you doin','how you doing',"how's it going",
                    "how have you been","how are you doing","how are you doin"],
        'response':['Good, thanks. What about you?','Fine. Thank you. And how are you?',
                    'Fine, thanks. You ok?']
    },
    {
        'message': ['yes', 'yeah', 'yep', 'yop',"good","great","ok", "fine", "im good",
                    "i am good", "i am fine", "im fine", "i am ok", "im ok"],
        'response':['Great!', "I'm glad to hear that!",'Cool']
    }
]


