import unittest

import app

# test class


class AppTests(unittest.TestCase):
    def test_my_function(self):
        self.assertIsNone(app.my_function())

    # def test_overly_complex_early_exit(self):
    #     self.assertIsNone(app.overly_complex(False, True, True, True))
    #     self.assertIsNone(app.overly_complex(True, False, True, True))

    # def test_overly_complex_deep_path(self):
    #     self.assertIsNone(app.overly_complex(True, True, True, True))

    def test_check_db(self):
        self.assertIsNone(app.check_db())

    def test_sonar_rules(self):
        self.assertEqual(app.test_sonar_rules(), "SuperSecretPassword123!")

    def test_is_even_returns_true_for_even_numbers(self):
        self.assertTrue(app.is_even(4))

    def test_is_even_returns_false_for_odd_numbers(self):
        self.assertFalse(app.is_even(5))


if __name__ == "__main__":
    unittest.main()
