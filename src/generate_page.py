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


    