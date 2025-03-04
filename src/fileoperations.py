from blocks import markdown_to_html_node
import os


def extract_title(markdown):
    if markdown[0]!="#":
        raise Exception("No Title Found")
    else:
        return markdown.split("\n")[0][2:]
    

def generate_page(from_path, template_path, dest_path,base_path):
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
    template=template.replace("href=\"/",f"href=\"{base_path}")
    template=template.replace("src=\"/",f"src=\"{base_path}")
    fp=open(dest_path,"w+")
    fp.write(template)
    fp.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,base_path):
    for val in os.listdir(dir_path_content):
        if ".md" in val:
            generate_page(os.path.join(dir_path_content,val),template_path,os.path.join(dest_dir_path,"index.html"),base_path)
        elif os.path.isdir(os.path.join(dir_path_content,val)):
            os.mkdir(os.path.join(dest_dir_path,val))
            generate_pages_recursive(os.path.join(dir_path_content,val),template_path,os.path.join(dest_dir_path,val),base_path)