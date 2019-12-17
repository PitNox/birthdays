import unittest
import birthdays


class TestBirthdays(unittest.TestCase):
    
    def setUp(self):  # Run this before each test, make sure the input is not a digit
        self.not_number = not_digit()      
  
    def test_reject_name_if_lower_case(self):  # Reject the lower-case names
        #Assume
        name = "donald trump"

        #Action
        result = birthdays.name_is_valid(name)

        #Assert
        self.assertEqual(self.not_number, True)
        self.assertFalse(result)

    def test_reject_name_if_too_long(self):  # Reject names longer than 20 char
        #Assume
        name = "Thisnameexceedstwentycharacters"

        #Action
        result = birthdays.name_is_valid(name)

        #Assert
        self.assertFalse(result)

    def test_accept_name_if_in_birthdays(self): # Consider valid the names present in dictionary
        #Assume
        name = 'Donald Trump'

        #Action
        result = birthdays.name_is_valid(name)

        #Assert
        self.assertTrue(result)

    def test_just_the_surname(self):  # Test the surname of a given name
        #Assume
        name = 'Albert Einstein'

        #Action
        result = birthdays.just_the_surname(name)

        #Assert
        self.assertEqual(result,"Einstein")

    def tearDown(self):  # Run this after each test
        self.not_number = None


if __name__ == '__main__':       # When running the module directly, run the code within the conditional
    unittest.main()
