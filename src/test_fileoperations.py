import unittest

from fileoperations import extract_title

class TestFileOperations(unittest.TestCase):
    def test_extract_title(self):
        Res=extract_title("# Hello\n")
        self.assertEqual(Res,"Hello")
    def test_extract_title_exception(self):
        with self.assertRaises(Exception):
            Res=extract_title("Hello")