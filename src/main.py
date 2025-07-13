import os
import shutil
from sys import argv

from copystatic import copy_files_recursive
from generate_page import generate_page, generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"


def main():
    basepath = "/"
    if len(argv) > 1:
        basepath = argv[1]
    print(f"Deleting {dir_path_public} directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print(f"Copying static files to {dir_path_public} directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    #generate_page("content/index.md", "template.html", "public/index.html", basepath)
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
