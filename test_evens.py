import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    def test_trow_error_if_value_is_in_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)
    
    def test_value_in_list(self):
        """
        Check if even_number_of_evens() returns False for empty list.
        Expected output: False.
        """
        self.assertEqual(even_number_of_evens([]), False)


if __name__ == "__main__":
    unittest.main()
