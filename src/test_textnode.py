import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eqlink(self):
        node=TextNode("This is a text node", TextType.LINK,"www.google.com.tr")
        node2=TextNode("This is a text node", TextType.LINK,"www.google.com.tr")
        self.assertEqual(node, node2)
    def test_noteq(self):
        node=TextNode("This is a text node", TextType.LINK)
        node2=TextNode("This is a text node", TextType.LINK,"www.google.com.tr")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()