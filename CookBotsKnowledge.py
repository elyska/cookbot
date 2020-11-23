# Data Module

import requests
import json

#######################################################################################
############# code from https://www.nltk.org/book/ch02.html ###########################
#######################################################################################

from nltk.corpus import stopwords
#nltk.download('stopwords')
uselessWords = stopwords.words('english')

#######################################################################################
############# end of code from https://www.nltk.org/book/ch02.html ####################
#######################################################################################

addUselessWords = ['would','not','cook','like','have','got','make','allergy','allergic', 'lowcarb', 'diet', 'low', 'carb', 'fat', 'lowfat', 'balanced', 'high', 'protein', 'highprotein', 'vegan', 'vegetarian','please','want','prepare','help','thanks','thank','nt','dont']

uselessWords = uselessWords + addUselessWords


availableDiets = ['balanced', 'high-protein', 'low-fat', 'low-carb']
availableHealthFilters = ['vegan', 'vegetarian', 'peanut-free', 'tree-nut-free', 'alcohol-free']

#######################################################################################
################################ code based on ########################################
#https://www.linkedin.com/learning/using-python-for-automation/using-api-keys?u=2039756
############# and https://developer.edamam.com/edamam-docs-recipe-api #################
#######################################################################################

def accessApi(keywords, healthList, dietList):
    '''This function takes 3 inputs: keywords is a string, healthList and dietList are lists of strings. It returns the data from API search as a dictionary.'''
    apiUrl = "https://api.edamam.com/search"
    parameters = {'app_id': '14a3021a', 'app_key': 'f89043d78ea9c82982e8b1ae788a04f9', 'q':keywords,'health':healthList,'diet':dietList}
    if len(healthList) == 0:
        parameters.pop('health') # delete key from dictionary if it is not needed
    if len(dietList) == 0:
        parameters.pop('diet') # delete keys from dictionary if it is not needed
    response = requests.get(apiUrl, params=parameters)
    searchJson = response.content # data in json format
    # print(type(searchJson))
    searchJson = searchJson.decode('utf-8') # convert searchJson (bytes) to string, necessary for some versions of Python
    output = json.loads(searchJson) # convert json to dictionary
    return output

#######################################################################################
############################ end of code based on #####################################
#https://www.linkedin.com/learning/using-python-for-automation/using-api-keys?u=2039756
############## and https://developer.edamam.com/edamam-docs-recipe-api ################
#######################################################################################

def dummyAccessApi():
    # this is the first recipe returned by accessApi('brownie', 'vegan', 'low-fat')
    x = {'from': 0, 'more': True, 'q': 'brownie', 'count': 48, 'to': 10, 'hits': [{'recipe': {'label': 'Coca Cola Brownies Recipe', 'url': 'http://www.seriouseats.com/recipes/2013/03/coca-cola-brownies-baking-with-coke-recipe.html', 'ingredients': [{'text': '1 1/4 cups (6 1/4 ounces) all purpose flour', 'weight': 177.18451953125, 'image': 'https://www.edamam.com/food-img/368/368077bbcab62f862a8c766a56ea5dd1.jpg'}, {'text': '1 2/3 cups (12 1/4 ounces) sugar', 'weight': 347.28165828125003, 'image': 'https://www.edamam.com/food-img/ecb/ecb3f5aaed96d0188c21b8369be07765.jpg'}, {'text': '2/3 cup cocoa powder', 'weight': 57.33333333333333, 'image': 'https://www.edamam.com/food-img/89a/89af89595db3cf2c3007f2b064c5fef6.jpg'}, {'text': '1/2 teaspoon salt', 'weight': 3.0, 'image': 'https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg'}, {'text': '1/2 teaspoon baking powder', 'weight': 2.3, 'image': 'https://www.edamam.com/food-img/a84/a8410ec57a2e62a1ad9955ac14d40af6.jpg'}, {'text': '1 can (12 ounces) Coca Cola', 'weight': 340.1942775, 'image': 'https://www.edamam.com/food-img/e86/e8658e93517d224d01b8e42b4f568a06.jpg'}], 'image': 'https://www.edamam.com/web-img/8ed/8ed74f2edb0bb1e8c90871ed5eb645ca.jpg', 'totalNutrients': {'CHOLE': {'label': 'Cholesterol', 'quantity': 0.0, 'unit': 'mg'}, 'ENERC_KCAL': {'label': 'Energy', 'quantity': 2246.696551317187, 'unit': 'kcal'}, 'RIBF': {'label': 'Riboflavin (B2)', 'quantity': 1.0794483748911459, 'unit': 'mg'}, 'FOLDFE': {'label': 'Folate equivalent (total)', 'quantity': 533.9536185026042, 'unit': 'µg'}, 'CHOCDF': {'label': 'Carbs', 'quantity': 548.6945817328907, 'unit': 'g'}, 'SUGAR.added': {'label': 'Sugars, added', 'quantity': 346.58709496468754, 'unit': 'g'}, 'P': {'label': 'Phosphorus', 'quantity': 874.3193755104166, 'unit': 'mg'}, 'FASAT': {'label': 'Saturated', 'quantity': 4.901436005273437, 'unit': 'g'}, 'VITD': {'label': 'Vitamin D', 'quantity': 0.0, 'unit': 'µg'}, 'ZN': {'label': 'Zinc', 'quantity': 5.250918658046875, 'unit': 'mg'}, 'WATER': {'label': 'Water', 'quantity': 330.2373030700313, 'unit': 'g'}, 'VITB6A': {'label': 'Vitamin B6', 'quantity': 0.1456145219270833, 'unit': 'mg'}, 'CA': {'label': 'Calcium', 'quantity': 280.33304672916665, 'unit': 'mg'}, 'THIA': {'label': 'Thiamin (B1)', 'quantity': 1.4356184783203128, 'unit': 'mg'}, 'FIBTG': {'label': 'Fiber', 'quantity': 26.00191536067708, 'unit': 'g'}, 'TOCPHA': {'label': 'Vitamin E', 'quantity': 0.4648577282552084, 'unit': 'mg'}, 'FOLAC': {'label': 'Folic acid', 'quantity': 272.864160078125, 'unit': 'µg'}, 'VITA_RAE': {'label': 'Vitamin A', 'quantity': 0.0, 'unit': 'µg'}, 'VITK1': {'label': 'Vitamin K', 'quantity': 1.9648868919270832, 'unit': 'µg'}, 'SUGAR': {'label': 'Sugars', 'quantity': 378.58425319250523, 'unit': 'g'}, 'VITC': {'label': 'Vitamin C', 'quantity': 0.0, 'unit': 'mg'}, 'K': {'label': 'Potassium', 'quantity': 1077.4519546140623, 'unit': 'mg'}, 'VITB12': {'label': 'Vitamin B12', 'quantity': 0.0, 'unit': 'µg'}, 'NA': {'label': 'Sodium', 'quantity': 1376.9432780734376, 'unit': 'mg'}, 'FAPU': {'label': 'Polyunsaturated', 'quantity': 0.9840387323307291, 'unit': 'g'}, 'FE': {'label': 'Iron', 'quantity': 16.984726240640622, 'unit': 'mg'}, 'FAT': {'label': 'Fat', 'quantity': 9.659113813572914, 'unit': 'g'}, 'FOLFD': {'label': 'Folate (food)', 'quantity': 69.73017733072916, 'unit': 'µg'}, 'NIA': {'label': 'Niacin (B3)', 'quantity': 11.713707366458333, 'unit': 'mg'}, 'FAMS': {'label': 'Monounsaturated', 'quantity': 2.7742838653255206, 'unit': 'g'}, 'PROCNT': {'label': 'Protein', 'quantity': 29.78093019516146, 'unit': 'g'}, 'MG': {'label': 'Magnesium', 'quantity': 326.00092763020825, 'unit': 'mg'}}, 'uri': 'http://www.edamam.com/ontologies/edamam.owl#recipe_66d89f834a3b8ea70563024cd9b1c6b8', 'cautions': ['Sulfites'], 'shareAs': 'http://www.edamam.com/recipe/coca-cola-brownies-recipe-66d89f834a3b8ea70563024cd9b1c6b8/brownie/vegan/low-fat', 'yield': 12.0, 'totalDaily': {'PROCNT': {'label': 'Protein', 'quantity': 59.56186039032292, 'unit': '%'}, 'CHOLE': {'label': 'Cholesterol', 'quantity': 0.0, 'unit': '%'}, 'TOCPHA': {'label': 'Vitamin E', 'quantity': 3.0990515217013894, 'unit': '%'}, 'FOLDFE': {'label': 'Folate equivalent (total)', 'quantity': 133.48840462565104, 'unit': '%'}, 'CHOCDF': {'label': 'Carbs', 'quantity': 182.89819391096358, 'unit': '%'}, 'P': {'label': 'Phosphorus', 'quantity': 124.90276793005951, 'unit': '%'}, 'VITD': {'label': 'Vitamin D', 'quantity': 0.0, 'unit': '%'}, 'ZN': {'label': 'Zinc', 'quantity': 47.7356241640625, 'unit': '%'}, 'VITB6A': {'label': 'Vitamin B6', 'quantity': 11.2011170713141, 'unit': '%'}, 'CA': {'label': 'Calcium', 'quantity': 28.033304672916667, 'unit': '%'}, 'THIA': {'label': 'Thiamin (B1)', 'quantity': 119.6348731933594, 'unit': '%'}, 'FIBTG': {'label': 'Fiber', 'quantity': 104.00766144270833, 'unit': '%'}, 'VITA_RAE': {'label': 'Vitamin A', 'quantity': 0.0, 'unit': '%'}, 'VITK1': {'label': 'Vitamin K', 'quantity': 1.6374057432725693, 'unit': '%'}, 'FASAT': {'label': 'Saturated', 'quantity': 24.507180026367188, 'unit': '%'}, 'VITC': {'label': 'Vitamin C', 'quantity': 0.0, 'unit': '%'}, 'K': {'label': 'Potassium', 'quantity': 22.924509672639623, 'unit': '%'}, 'VITB12': {'label': 'Vitamin B12', 'quantity': 0.0, 'unit': '%'}, 'NA': {'label': 'Sodium', 'quantity': 57.372636586393234, 'unit': '%'}, 'ENERC_KCAL': {'label': 'Energy', 'quantity': 112.33482756585936, 'unit': '%'}, 'FE': {'label': 'Iron', 'quantity': 94.35959022578123, 'unit': '%'}, 'FAT': {'label': 'Fat', 'quantity': 14.860175097804483, 'unit': '%'}, 'NIA': {'label': 'Niacin (B3)', 'quantity': 73.21067104036459, 'unit': '%'}, 'RIBF': {'label': 'Riboflavin (B2)', 'quantity': 83.03449037624199, 'unit': '%'}, 'MG': {'label': 'Magnesium', 'quantity': 77.61926848338291, 'unit': '%'}}, 'digest': [{'label': 'Fat', 'schemaOrgTag': 'fatContent', 'unit': 'g', 'tag': 'FAT', 'total': 9.659113813572914, 'sub': [{'label': 'Saturated', 'schemaOrgTag': 'saturatedFatContent', 'unit': 'g', 'tag': 'FASAT', 'total': 4.901436005273437, 'hasRDI': True, 'daily': 24.507180026367188}, {'label': 'Trans', 'schemaOrgTag': 'transFatContent', 'unit': 'g', 'tag': 'FATRN', 'total': 0.0, 'hasRDI': False, 'daily': 0.0}, {'label': 'Monounsaturated', 'schemaOrgTag': None, 'unit': 'g', 'tag': 'FAMS', 'total': 2.7742838653255206, 'hasRDI': False, 'daily': 0.0}, {'label': 'Polyunsaturated', 'schemaOrgTag': None, 'unit': 'g', 'tag': 'FAPU', 'total': 0.9840387323307291, 'hasRDI': False, 'daily': 0.0}], 'hasRDI': True, 'daily': 14.860175097804483}, {'label': 'Carbs', 'schemaOrgTag': 'carbohydrateContent', 'unit': 'g', 'tag': 'CHOCDF', 'total': 548.6945817328907, 'sub': [{'label': 'Carbs (net)', 'schemaOrgTag': None, 'unit': 'g', 'tag': 'CHOCDF.net', 'total': 522.6926663722136, 'hasRDI': False, 'daily': 0.0}, {'label': 'Fiber', 'schemaOrgTag': 'fiberContent', 'unit': 'g', 'tag': 'FIBTG', 'total': 26.00191536067708, 'hasRDI': True, 'daily': 104.00766144270833}, {'label': 'Sugars', 'schemaOrgTag': 'sugarContent', 'unit': 'g', 'tag': 'SUGAR', 'total': 378.58425319250523, 'hasRDI': False, 'daily': 0.0}, {'label': 'Sugars, added', 'schemaOrgTag': None, 'unit': 'g', 'tag': 'SUGAR.added', 'total': 346.58709496468754, 'hasRDI': False, 'daily': 0.0}], 'hasRDI': True, 'daily': 182.89819391096358}, {'label': 'Protein', 'schemaOrgTag': 'proteinContent', 'unit': 'g', 'tag': 'PROCNT', 'total': 29.78093019516146, 'hasRDI': True, 'daily': 59.56186039032292}, {'label': 'Cholesterol', 'schemaOrgTag': 'cholesterolContent', 'unit': 'mg', 'tag': 'CHOLE', 'total': 0.0, 'hasRDI': True, 'daily': 0.0}, {'label': 'Sodium', 'schemaOrgTag': 'sodiumContent', 'unit': 'mg', 'tag': 'NA', 'total': 1376.9432780734376, 'hasRDI': True, 'daily': 57.372636586393234}, {'label': 'Calcium', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'CA', 'total': 280.33304672916665, 'hasRDI': True, 'daily': 28.033304672916667}, {'label': 'Magnesium', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'MG', 'total': 326.00092763020825, 'hasRDI': True, 'daily': 77.61926848338291}, {'label': 'Potassium', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'K', 'total': 1077.4519546140623, 'hasRDI': True, 'daily': 22.924509672639623}, {'label': 'Iron', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'FE', 'total': 16.984726240640622, 'hasRDI': True, 'daily': 94.35959022578123}, {'label': 'Zinc', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'ZN', 'total': 5.250918658046875, 'hasRDI': True, 'daily': 47.7356241640625}, {'label': 'Phosphorus', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'P', 'total': 874.3193755104166, 'hasRDI': True, 'daily': 124.90276793005951}, {'label': 'Vitamin A', 'schemaOrgTag': None, 'unit': 'µg', 'tag': 'VITA_RAE', 'total': 0.0, 'hasRDI': True, 'daily': 0.0}, {'label': 'Vitamin C', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'VITC', 'total': 0.0, 'hasRDI': True, 'daily': 0.0}, {'label': 'Thiamin (B1)', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'THIA', 'total': 1.4356184783203128, 'hasRDI': True, 'daily': 119.6348731933594}, {'label': 'Riboflavin (B2)', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'RIBF', 'total': 1.0794483748911459, 'hasRDI': True, 'daily': 83.03449037624199}, {'label': 'Niacin (B3)', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'NIA', 'total': 11.713707366458333, 'hasRDI': True, 'daily': 73.21067104036459}, {'label': 'Vitamin B6', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'VITB6A', 'total': 0.1456145219270833, 'hasRDI': True, 'daily': 11.2011170713141}, {'label': 'Folate equivalent (total)', 'schemaOrgTag': None, 'unit': 'µg', 'tag': 'FOLDFE', 'total': 533.9536185026042, 'hasRDI': True, 'daily': 133.48840462565104}, {'label': 'Folate (food)', 'schemaOrgTag': None, 'unit': 'µg', 'tag': 'FOLFD', 'total': 69.73017733072916, 'hasRDI': False, 'daily': 0.0}, {'label': 'Folic acid', 'schemaOrgTag': None, 'unit': 'µg', 'tag': 'FOLAC', 'total': 272.864160078125, 'hasRDI': False, 'daily': 0.0}, {'label': 'Vitamin B12', 'schemaOrgTag': None, 'unit': 'µg', 'tag': 'VITB12', 'total': 0.0, 'hasRDI': True, 'daily': 0.0}, {'label': 'Vitamin D', 'schemaOrgTag': None, 'unit': 'µg', 'tag': 'VITD', 'total': 0.0, 'hasRDI': True, 'daily': 0.0}, {'label': 'Vitamin E', 'schemaOrgTag': None, 'unit': 'mg', 'tag': 'TOCPHA', 'total': 0.4648577282552084, 'hasRDI': True, 'daily': 3.0990515217013894}, {'label': 'Vitamin K', 'schemaOrgTag': None, 'unit': 'µg', 'tag': 'VITK1', 'total': 1.9648868919270832, 'hasRDI': True, 'daily': 1.6374057432725693}, {'label': 'Sugar alcohols', 'schemaOrgTag': None, 'unit': 'g', 'tag': 'Sugar.alcohol', 'total': 0.0, 'hasRDI': False, 'daily': 0.0}, {'label': 'Water', 'schemaOrgTag': None, 'unit': 'g', 'tag': 'WATER', 'total': 330.2373030700313, 'hasRDI': False, 'daily': 0.0}], 'healthLabels': ['Vegan', 'Vegetarian', 'Peanut-Free', 'Tree-Nut-Free', 'Alcohol-Free'], 'calories': 2246.696551317187, 'totalWeight': 927.2937886458334, 'ingredientLines': ['1 1/4 cups (6 1/4 ounces) all purpose flour', '1 2/3 cups (12 1/4 ounces) sugar', '2/3 cup cocoa powder', '1/2 teaspoon salt', '1/2 teaspoon baking powder', '1 can (12 ounces) Coca Cola'], 'dietLabels': ['Low-Fat'], 'source': 'Serious Eats', 'totalTime': 40.0}, 'bookmarked': False, 'bought': False}]}
    return x

def searchOutput(keywords, healthList, dietList):
    '''This function takes 3 inputs: keywords is a string, healthList and dietList are lists of strings. It returns only useful data (label, url, dietLabels,
    healthLabels, ingredientLines) for each recipe from API search as a list of dictionaries.'''
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
        'message': ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'gm'],
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
        'message': ['how are you', 'how you doin','how you doing',"how's it going","how have you been","how are you doing","how are you doin"],
        'response':['Good, thanks. What about you?', 'Fine. Thank you. And how are you?','Fine, thanks. You ok?']
    },
    {
        'message': ['yes', 'yeah', 'yep', 'yop',"good","great","ok", "fine", "im good", "i am good", "i am fine", "im fine", "i am ok", "im ok"],
        'response':['Great!', "I'm glad to hear that!",'Cool']
    }
]



