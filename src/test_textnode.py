import unittest

from textnode import TextNode, TextType,text_node_to_html_node
from texttonode import *


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
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_boldtext(self):
        node=TextNode("This is a Bold Text",TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a Bold Text")

    def test_link(self):
        node=TextNode("This is a link",TextType.LINK,"google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"], "google.com")

    def test_markdown_to_textnode(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(new_nodes[0]),'TextNode(This is text with a ,normal,None)')
        self.assertEqual(str(new_nodes[1]),'TextNode(code block,code,None)')
        self.assertEqual(str(new_nodes[2]),'TextNode( word,normal,None)')

    def test_multiple_block(self):
        node = TextNode("This is **text** with a **code** block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(new_nodes[0]),'TextNode(This is ,normal,None)')
        self.assertEqual(str(new_nodes[1]),'TextNode(text,bold,None)')
        self.assertEqual(str(new_nodes[2]),'TextNode( with a ,normal,None)')
        self.assertEqual(str(new_nodes[3]),'TextNode(code,bold,None)')
        self.assertEqual(str(new_nodes[4]),'TextNode( block word,normal,None)')
    def test_multiple_nodes(self):
        node = TextNode("This is **text** with a **code** block word", TextType.TEXT)
        node2=TextNode("This is a second text with a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node,node2], "**", TextType.BOLD)
        self.assertEqual(str(new_nodes[0]),'TextNode(This is ,normal,None)')
        self.assertEqual(str(new_nodes[1]),'TextNode(text,bold,None)')
        self.assertEqual(str(new_nodes[2]),'TextNode( with a ,normal,None)')
        self.assertEqual(str(new_nodes[3]),'TextNode(code,bold,None)')
        self.assertEqual(str(new_nodes[4]),'TextNode( block word,normal,None)')
        self.assertEqual(str(new_nodes[5]),'TextNode(This is a second text with a ,normal,None)')
        self.assertEqual(str(new_nodes[6]),'TextNode(code block,bold,None)')
        self.assertEqual(str(new_nodes[7]),'TextNode( word,normal,None)')
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) ![image](https://i.imgur.com/zjjcJKZ.png) ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),("image", "https://i.imgur.com/zjjcJKZ.png"),("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_link(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_link_not_images(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://google.com.tr) and an image ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://google.com.tr")], matches)
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
            "[image](https://i.imgur.com/zjjcJKZ.png) [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
            "This is text with an no link and another no link",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an no link and another no link", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()