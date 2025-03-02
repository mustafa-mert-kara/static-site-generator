import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_Node(self):
        node=HTMLNode("p","Deneme","List of Children","Propstmp")
        self.assertEqual(str(node),f"tag=p, value=Deneme, children=List of Children, props=Propstmp")

    def test_props(self):
        node=HTMLNode(props={
    "href": "https://www.google.com",
    "target": "_blank",})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')
    def test_None(self):
        node=HTMLNode("p")
        self.assertEqual(str(node),f"tag=p, value=None, children=None, props=None")
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leafnode_error(self):
        with self.assertRaises(ValueError):
            node=LeafNode("p",None)
            node.to_html()
    def test_leaf_to_html_p(self):
        node = LeafNode("", "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
