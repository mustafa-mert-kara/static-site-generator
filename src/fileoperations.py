from blocks import markdown_to_html_node

def extract_title(markdown):
    if markdown[0]!="#":
        raise Exception("No Title Found")
    else:
        return markdown.split("\n")[0][2:]
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as fp:
        markdown=fp.read()
    with open(template_path) as fp:
        template=fp.read()
    
    html_node=markdown_to_html_node(markdown)
    html_string=html_node.to_html()
    title=extract_title(markdown)
    split_template=template.split("""{{ Title }}""")
    template=f"{split_template[0]}{title}{split_template[1]}"
    split_template=template.split("{{ Content }}")
    template=f"{split_template[0]}{html_string}{split_template[1]}"
    fp=open(dest_path,"w")
    fp.write(template)
    fp.close()
    