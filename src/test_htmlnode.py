import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag here", "value here", None, {"href":"https://site.url", "target":"_blank"})
        node2 = HTMLNode("tag here", "value here", None, {"href":"https://site.url", "target":"_blank"})
        node_props = node.props_to_html()
        node2_props = node2.props_to_html()
        #print(f"node: {node_props}")
        #print(f"node2: {node2_props}")
        #self.assertEqual(node, node2)
        self.assertEqual(node_props, node2_props)

    def test_noteq(self):
        node = HTMLNode("tag here", "value here")
        node2 = HTMLNode("tag here", "other value here", ["child1", "child2"], {"href":"https://site.url", "target":"_blank"})
        #node_props = node.props_to_html()
        #node2_props = node2.props_to_html()
        #print(f"node: {node_props}")
        #print(f"node2: {node2_props}")
        self.assertNotEqual(node, node2)

    def test_noteq2(self):
        node = HTMLNode("tag here, no values")
        node2 = HTMLNode("tag here", "value here")
        #node_props = node.props_to_html()
        #node2_props = node2.props_to_html()
        #print(f"node: {node_props}")
        #print(f"node2: {node2_props}")
        self.assertNotEqual(node, node2)

    def test_leaftohtml(self):
        node = LeafNode("p", "This is a paragraph of text.").to_html()
        intent = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node, intent)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_props(self):
        grandchild_node = LeafNode("b", "grandchild", {"class":"highlight"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b class=\"highlight\">grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()