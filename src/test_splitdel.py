import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from splitdel import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text, "This is text with a ") 
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code block") 
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " word") 
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This is text with a ") 
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "bold") 
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " word") 
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_ital(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text, "This is text with an ") 
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "italic") 
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, " word") 
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_nottext(self):
        node = TextNode("This is all bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This is all bold text") 
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)

    def test_unmatchdelim(self):
        node = TextNode("This is text with an _italic word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_nodelimit(self):
        node = TextNode("This is text with no delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text, "This is text with no delimiter") 
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()