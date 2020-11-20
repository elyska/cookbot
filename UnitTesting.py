# tests

import unittest
from CookBotsBrain import*
from CookBotsKnowledge import*

class TestBot(unittest.TestCase):
    # meaningful input, recipes found
    #def testAccessApi1(self):
    #    self.assertIn('recipe',dummyAccessApi()['hits'][0])
    # meaningless input, no recipes found
    #def testAccessApi2(self):
    #    self.assertNotIn('recipe',dummyAccessApi()['hits'][0])

    # meaningful input, recipes found
    def testAccessApi1(self):
        self.assertIn('recipe',accessApi('pizza', ['vegetarian'], [])['hits'][0])
    # meaningless input, no recipes found
    def testAccessApi2(self):
        self.assertEqual(0,len(accessApi('hdfhhbdjhrw', [], [])['hits']))
    # multiple filters
    def testAccessApi3(self):
        apiCall = accessApi('pizza', ['vegetarian', 'vegan'], ['low-fat'])
        self.assertIn('Vegan',apiCall['hits'][0]['recipe']['healthLabels'])
        self.assertIn('Vegetarian', apiCall['hits'][0]['recipe']['healthLabels'])
        self.assertIn('Low-Fat', apiCall['hits'][0]['recipe']['dietLabels'])





if __name__ == '__main__':
    unittest.main()


