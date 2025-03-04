import unittest
from blocks import *

class TestBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_block_types(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        blockTypes=list(map(block_to_blocktype,blocks))
        self.assertListEqual(blockTypes,[
             BlockType.PARAGRAPH,
             BlockType.PARAGRAPH,
             BlockType.ULIST
        ])

    def test_block_types2(self):
        md = """
#This is **bolded** paragraph

>This is another paragraph with _italic_ text and `code` here

```This is the same paragraph on a new line```

1. This is a list
2. with items
        """
        blocks = markdown_to_blocks(md)
        blockTypes=list(map(block_to_blocktype,blocks))
        self.assertListEqual(blockTypes,[
             BlockType.HEADING,
             BlockType.QUOTE,
             BlockType.CODE,
             BlockType.OLIST
        ])
    
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_link_generation(self):
        md="""
## Blog posts

- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
"""
        node=markdown_to_html_node(md)
        html=node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Blog posts</h2><ul><li><a href=\"/blog/glorfindel\">Why Glorfindel is More Impressive than Legolas</a></li><li><a href=\"/blog/tom\">Why Tom Bombadil Was a Mistake</a></li></ul></div>",
        )













if __name__=="__main__":
    unittest.main()