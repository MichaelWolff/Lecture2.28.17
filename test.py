import unittest
import functions

class ChatbotResponseTest(unittest.TestCase):
    def test_hello_command(self):
        response = functions.get_chatbot_response("!! say Hey there!")
        self.assertEqual(response, "Hey there!")
        
    def test_say_command(self):
        response = functions.get_chatbot_response("!! say applesauces aint saucy")
        self.assertEquals(response, "applesauces aint saucy")
        
if __name__ == '__main__':
    unittest.main()