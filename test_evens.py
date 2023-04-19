import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    def test_trow_error_if_value_is_in_not_list(self):
        """
        Tests whether the even_number_of_evens function raises a TypeError
        when an integer value is passed instead of a list, using the
        assertRaises method of the unittest module
        """
        self.assertRaises(TypeError, even_number_of_evens, 4)
       
    def test_value_in_list(self):
        # Check if function returns False for empty list.
        # Expected output: True.
        self.assertEqual(even_number_of_evens([]), False)
        # Check if function returns True if two even no. in a list
        # Expected output: True.
        self.assertEqual(even_number_of_evens([2, 4]), True)
        # Check if function returns False if one even no. in a list
        # Expected output: Flase.
        self.assertEqual(even_number_of_evens([2]), False)
        # Check if function returns Fasle if odd no. in a list
        # Expected output: Flase.
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)

             


if __name__ == "__main__":
    unittest.main()
