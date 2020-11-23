#  Interface Module to run on Discord

from CookBotsBrain import*
import discord

#######################################################################################
############# code inspired by https://pypi.org/project/discord.py/####################
#######################################################################################

class MyClient(discord.Client):

    q1asked = False # indicates if the first question (about allergies) was asked
    q2asked = False # indicates if the question about allergies diets was asked
    userInput = '' # to store keywords from the user during the conversation
    firstRecipeFound = False # to indicate if the first recipe was found
    recipeNumber = 0 # it is used as an index in the list of found recipes

    def resetAttributes(self):
        '''This method resets the attributes for a new recipe search.'''
        self.firstRecipeFound = False
        self.q1asked = False
        self.q2asked = False
        self.userInput = ''
        self.recipeNumber = 0

    async def on_ready(self):
        async def on_ready(self):
            print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
       
        else:
            inp = message.content # a new message from the user
            inMemory = fixedAnswer(inp)
            if inMemory != '' and self.firstRecipeFound == False: # if there is a fixed answer to the message and the user hasn't asked for a new recipe
                await message.channel.send(inMemory)
            elif 'help' in inp: # if the user asks for help
                await message.channel.send('I can find a recipe for you based on your diets and allergies.')
            else:
                self.userInput = self.userInput + ' ' + inp # add keywords, necessary to store previous messages if the bot has to ask additional questions
                if extractHealthFilters(self.userInput) == [] and self.q1asked == False: # if the user hasn't mentioned any allergies and the bot hasn't asked about them
                    await message.channel.send('Ok. Would you like to add any allergy filters? And let me know if you are looking for a vegan or vegetarian recipe.') # additional question 1
                    self.q1asked = True # indicates that the bot has already asked additional question 1
                    self.userInput = self.userInput + ' ' + str(extractHealthFilters(inp)) +'allergy' # add the health filters to the keywords
                elif extractDiets(self.userInput) == [] and self.q2asked == False:
                    await message.channel.send('Would you like to add any diet filters? Like low-fat, low-carb, high-protein, balanced... ') # additional question 2
                    self.q2asked = True # indicates that the bot has already asked additional question 2
                    self.userInput = self.userInput + ' ' + str(extractDiets(inp)) # add the diet filters to the keywords
                elif self.firstRecipeFound == False: # if the user hasn't asked for a new recipe yet
                    answer = semiIntelligentAnswer(self.userInput,self.recipeNumber)
                    await message.channel.send(answer)
                    self.firstRecipeFound = True # indicates that the first recipe was already found
                    if answer == "I am sorry. I couldn't find a recipe for you." or "I am sorry. Search for another recipe or try this one" in answer:
                        # reset the attributes for a new recipe search
                        self.resetAttributes()
                else: # after a recipe is found
                    if 'no' in inp.lower(): # if the user doesn't like the first recipe
                        self.recipeNumber += 1 # increase the index in the list of recipes
                        answer = semiIntelligentAnswer(self.userInput, self.recipeNumber)
                        if answer == "I am sorry. I couldn't find a recipe for you.":
                            # reset the attributes for a new recipe search
                            self.resetAttributes()
                    else:
                        inMemory = fixedAnswer(inp)
                        if inMemory != '' and self.firstRecipeFound == True: # if there is a fixed answer to the message and the first recipe was found
                            answer = inMemory
                        else: # if the bot doesn't understand
                            answer = 'Hmm'
                        # reset the attributes for a new recipe search
                        self.resetAttributes()
                    await message.channel.send(answer)

client = MyClient()
client.run('Nzc2ODQ4NjQ5MTk2MDExNTQw.X662rw.jHrbtM80K0DeSfdH-sp09TgUqrA')

#######################################################################################
########## end of code inspired by https://pypi.org/project/discord.py/################
#######################################################################################
