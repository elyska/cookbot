# Tests

import unittest
from CookBotsBrain import*
from CookBotsKnowledge import*

class TestBot(unittest.TestCase):
    def testDummyAccessApi(self):
        self.assertIn('recipe',dummyAccessApi()['hits'][0])

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

    def testSeparateContractions(self):
        self.assertIn("n't",separateContractions(["i", "don't", "like", "tomatoes"]))
        self.assertIn("d",
                      separateContractions(["i'd", "like","to","make", "a", "pizza"]))

    def testMeaningfulWords(self):
        self.assertEqual(["tomatoes"],
                         meaningfulWords("I don't like tomatoes."))
        self.assertEqual(["pizza","peanuts"],
                         meaningfulWords("I'd like to make a pizza. "
                                         "I am allergic to peanuts"))
        self.assertEqual(["apple", "tomatoes"],
                         meaningfulWords("I've got an apple. I don't have tomatoes."))

    def testProcessUserMessage(self):
        self.assertEqual("hola vsssgr jzrfasdf skirj",
                         processUserMessage("Hola! (vsss)gr JZRFa<sdf: ski'rj."))


if __name__ == '__main__':
    unittest.main()


