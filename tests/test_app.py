import unittest

import app


class AppTests(unittest.TestCase):
    def test_my_function(self):
        self.assertIsNone(app.my_function())

    def test_overly_complex_early_exit(self):
        self.assertIsNone(app.overly_complex(False, True, True, True, True))
        self.assertIsNone(app.overly_complex(True, False, True, True, True))

    def test_overly_complex_deep_path(self):
        self.assertIsNone(app.overly_complex(True, True, True, True, True))

    def test_check_db(self):
        self.assertIsNone(app.check_db())

    def test_sonar_rules(self):
        self.assertEqual(app.test_sonar_rules(), "SuperSecretPassword123!")


if __name__ == "__main__":
    unittest.main()
