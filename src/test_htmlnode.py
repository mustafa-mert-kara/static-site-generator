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
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_multiple_children(self):
        child1=LeafNode("p","child1")
        child2=LeafNode("b","child2")
        parent1=ParentNode("p",[child1,child2])
        self.assertEqual(parent1.to_html(),"<p><p>child1</p><b>child2</b></p>")







if __name__=="__main__":
    unittest.main()
