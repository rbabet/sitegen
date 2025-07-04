from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    mytextnode = TextNode("Some anchor text", "link", "https://www.site.url")
    print(f"mytextnode is {mytextnode}")

if __name__ == "__main__":
    main()
