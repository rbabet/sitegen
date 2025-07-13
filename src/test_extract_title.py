import unittest

from extract_title import extract_title


class TestTextNode(unittest.TestCase):
    def test_with_h1_and_trailing_spaces(self):
        title = extract_title("# Tolkien Fan Club   ")
        self.assertEqual(title, "Tolkien Fan Club")

    def test_with_bad_h1(self):
        with self.assertRaises(Exception):
            extract_title("## Tolkien Fan Club")

if __name__ == "__main__":
    unittest.main()