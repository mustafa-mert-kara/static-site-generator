from enum import Enum
from textnode import *
from texttonode import *


class BlockType(Enum):
    PARAGRAPH="paragraph"
    HEADING="heading"
    CODE="code"
    QUOTE="quote"
    ULIST="unordered_list"
    OLIST="ordered_list"


def markdown_to_blocks(markdown):
    blocks=markdown.split("\n\n")
    blocks=list(filter(lambda x: x!='', map(lambda x: x.strip().strip("\n") ,blocks)))
    return blocks

def block_to_blocktype(block):
    if block is None or block =='':
        return None
    if block[0]=="#":
        return BlockType.HEADING
    elif block[:3]=="```" and block[-3:]=="```":
        return BlockType.CODE
    elif block[0]==">":
        return BlockType.QUOTE
    elif block[0]=="-":
        return BlockType.ULIST
    elif block[0].isdigit() and block[1]==".":
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH
    

def markdown_to_html_node(markdown):
    blocks=markdown_to_blocks(markdown)
    html_code=""
    
    Parent_of_blocks=[]
    for block in blocks:
        match block_to_blocktype(block):
            case BlockType.PARAGRAPH:
                children_of_blocks=text_to_children(block)
                block_parent=ParentNode("p",children_of_blocks)
                Parent_of_blocks.append(block_parent)
            case BlockType.HEADING:
                headin_tier=0
                while block[headin_tier]=="#":
                    headin_tier+=1
                children_of_blocks=text_to_children(block[headin_tier:])
                block_parent=ParentNode(f"h{str(headin_tier)}",children_of_blocks)
                Parent_of_blocks.append(block_parent)
            case  BlockType.QUOTE:
                children_of_blocks=text_to_children(block[1:])
                block_parent=ParentNode("blockquote",children_of_blocks)
                Parent_of_blocks.append(block_parent)
            case  BlockType.ULIST:
                list_items=block.split("\n")
                children_of_blocks=[]
                for item in list_items:
                    item_nodes=text_to_children(item[1:])
                    children_of_blocks.append(Parent_of_blocks("li",item_nodes))
                Parent_of_blocks.append(ParentNode("ul",children_of_blocks))
            case  BlockType.OLIST:
                list_items=block.split("\n")
                children_of_blocks=[]
                for item in list_items:
                    item_nodes=text_to_children(item[2:])
                    children_of_blocks.append(Parent_of_blocks("li",item_nodes))
                Parent_of_blocks.append(ParentNode("ol",children_of_blocks))
            case  BlockType.CODE:
                code_text=block[3:-3]
                if code_text[0]=="\n":
                    code_text=code_text[1:]
                html_node=text_node_to_html_node(TextNode(code_text,type=TextType.CODE))
                block_parent=ParentNode("pre",[html_node])
                Parent_of_blocks.append(block_parent)

    return ParentNode("div",Parent_of_blocks)

def text_to_children(text):
    text_nodes=text_to_textnode(text)
    html_children=list(map(text_node_to_html_node,text_nodes))
    return html_children