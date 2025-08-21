import unittest

class Test_tring_caclulator(unittest.TestCase):
    def test_empty_string_retrun_zero(self):
        # arrange 
        input = ""
        expected_value = 0
        # action
        actual_value = add(input)
        #assert
        self.assertEqual(actual_value, expected_value)
      
if __name__ == "__main__":
    unittest.main()
