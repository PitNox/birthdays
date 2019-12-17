"""This is a test suit used for testing the code in the library file
birthday.py.

A class that derives from unittest.TestCase has been defined
and it represents a test suit.

Each method in the class whose name starts with test is a test case.

So in this test suit we have:

- a test for lower case names;

- a test for too long names;

- a test for checking if the name is present in the birthday dictionary
contained in the birthday.py module;

- a test for returning just the surname of the full name given.



A setUp function has been created for testing whether the input name is a
digit or not,

which is run before each test. And a tearDown to clean up everything.



The if __name__ == '__main__' has been to say: if this file is directly run by
python or being imported,

run unittest.main().

"""

import unittest

import birthdays


class TestBirthdays(unittest.TestCase):

    """Creating test cases is accomplished by subclassing unittest.TestCase."""

    def setUp(self):

        """Run this before each test, to make sure the input given is not a
        digit."""

        self.not_number = birthdays.not_digit('This is a string')

    def test_reject_name_if_lower_case(self):
        """Reject the lower-case names."""

        # Assume
        name = "donald trump"

        # Action

        result = birthdays.name_is_valid(name)

        # Assert

        self.assertEqual(self.not_number, True)

        self.assertFalse(result)

    def test_reject_name_if_too_long(self):
        """Reject names longer than 20 char."""
        # Assume

        name = "Thisnameexceedstwentycharacters"

        # Action

        result = birthdays.name_is_valid(name)

        # Assert

        self.assertFalse(result)

    def test_accept_name_if_in_birthdays(self):

        """Consider valid the names present in dictionary."""

        # Assume

        name = 'Donald Trump'

        # Action

        result = birthdays.name_is_valid(name)

        # Assert

        self.assertTrue(result)

    def test_just_the_surname(self):

        """Test the surname of a given name."""

        # Assume

        name = 'Albert Einstein'

        # Action

        result = birthdays.just_the_surname(name)

        # Assert

        self.assertEqual(result, "Einstein")

    def tearDown(self):

        """Run this after each test."""

        self.not_number = None

if __name__ == '__main__':  # When running the module directly, run the code
                            # within the conditional

    unittest.main()

