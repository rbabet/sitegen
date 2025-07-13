import os

from blocktype import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as md_file:
        md_lines = md_file.read()

    with open(template_path) as template_file:
        template_lines = template_file.read()

    md_html = markdown_to_html_node(md_lines).to_html()
    title = extract_title(md_lines)

    template_lines = template_lines.replace('{{ Title }}', title)
    template_lines = template_lines.replace('{{ Content }}', md_html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as target_file:
        target_file.write(template_lines)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    cur_dir = os.listdir(dir_path_content)
    for item in cur_dir:
        new_source = os.path.join(dir_path_content, item)
        new_dest = os.path.join(dest_dir_path, item)
        if os.path.isfile(new_source):
            if new_source.endswith(".md"):
                new_dest = os.path.splitext(new_dest)[0] + ".html"
                generate_page(new_source, template_path, new_dest)
        else:
            generate_pages_recursive(new_source, template_path, new_dest)


    