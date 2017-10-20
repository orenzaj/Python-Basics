from string_fun import get_anagram

class AnagramTestcase(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaise(ValueError):
            get_anagram("")

    def test_no_arguments(self):
        with self.assertRaise(ValueError):
            get_anagram()
