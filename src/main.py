from textnode import *
from fileoperations import generate_page
import os
import shutil
from pathlib import Path



def move_files(root,destination):    
    for val in os.listdir(root):
        if os.path.isfile(os.path.join(root,val)):
            shutil.copy(os.path.join(root,val),destination)    
        elif os.path.isdir(os.path.join(root,val)):
            os.mkdir(os.path.join(destination,val),)
            move_files(os.path.join(root,val),os.path.join(destination,val))

def build_file_structure(root,destination):
    
    if not os.path.isdir(destination):
        os.mkdir(destination)
    else:
        shutil.rmtree(destination)
        os.mkdir(destination)
    
    move_files(root,destination)

def main():
    cwd=Path(__file__).parent.parent
    build_file_structure(os.path.join(cwd,"static"),os.path.join(cwd,"public"))
    generate_page(os.path.join(cwd,"content","index.md"),os.path.join(cwd,"template.html"),os.path.join(cwd,"public","index.html"))

if __name__=="__main__":
    main()