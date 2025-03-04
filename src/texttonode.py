from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    for node in old_nodes: 
        if node.text_type!=TextType.TEXT:   
            new_nodes.append(node)
        else:
            split_nodes=node.text.split(delimiter)
            if len(split_nodes)%2==0:
                raise Exception("Improper syntax")
            for i in range(len(split_nodes)):
                if i%2==0:
                    new_nodes.append(TextNode(split_nodes[i],TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_nodes[i],text_type))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)


def split_nodes_image(old_nodes):
    new_nodes=[]
    for node in old_nodes: 
        if node.text_type!=TextType.TEXT:   
            new_nodes.append(node)
        else:
            images=extract_markdown_images(node.text)
            curr_text=node.text
            for image in images:
                split_nodes=curr_text.split(f"![{image[0]}]({image[1]})",1)
                if split_nodes[0]!='':
                    new_nodes.append(TextNode(split_nodes[0],TextType.TEXT))
                new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))
                curr_text=split_nodes[1]
            if curr_text!='':
                new_nodes.append(TextNode(curr_text,TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes=[]
    for node in old_nodes: 
        if node.text_type!=TextType.TEXT:   
            new_nodes.append(node)
        else:
            links=extract_markdown_links(node.text)
            curr_text=node.text
            for link in links:
                split_nodes=curr_text.split(f"[{link[0]}]({link[1]})",1)
                if split_nodes[0]!='':
                    new_nodes.append(TextNode(split_nodes[0],TextType.TEXT))
                new_nodes.append(TextNode(link[0],TextType.LINK,link[1]))
                curr_text=split_nodes[1]
            if curr_text!='':
                new_nodes.append(TextNode(curr_text,TextType.TEXT))

    return new_nodes

def text_to_textnode(text):
    old_node=TextNode(text.strip().strip("\n").replace("\n"," "),TextType.TEXT)
    new_node=split_nodes_delimiter([old_node],"**",TextType.BOLD)
    
    new_node=split_nodes_delimiter(new_node,"_",TextType.ITALIC)
    
    new_node=split_nodes_delimiter(new_node,"`",TextType.CODE)
    
    new_node=split_nodes_image(new_node)
    new_node=split_nodes_link(new_node)

    return new_node




