import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node with a url", TextType.TEXT, "https://site.url")
        self.assertNotEqual(node, node2)

    def test_noteq2(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a plain text node", TextType.TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()