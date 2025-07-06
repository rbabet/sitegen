import unittest
from blocktype import (
    BlockType,
    block_to_block_type,
)

class TestTextNode(unittest.TestCase):
    def test_blocktype_heading(self):
        thisblock = block_to_block_type("# This is a heading")
        self.assertEqual(thisblock, BlockType.HEADING)

    def test_blocktype_code(self):
        thisblock = block_to_block_type("```This is a code block\nwith lines\nof code```")
        self.assertEqual(thisblock, BlockType.CODE)

    def test_blocktype_quote(self):
        thisblock = block_to_block_type("> This is a quote block\n> with quote lines")
        self.assertEqual(thisblock, BlockType.QUOTE)

    def test_blocktype_unordered_list(self):
        thisblock = block_to_block_type("- This is an unordered list\n- with multiple lines")
        self.assertEqual(thisblock, BlockType.UNORDERED_LIST)

    def test_blocktype_ordered_list(self):
        thisblock = block_to_block_type("1. This is an ordered list\n2. with multiple ordered lines\n3. and three items")
        self.assertEqual(thisblock, BlockType.ORDERED_LIST)

    def test_blocktype_ordered_list_fail(self):
        thisblock = block_to_block_type("1. This is not an ordered list\n3. with badly ordered lines\n3. and three stupid items")
        self.assertEqual(thisblock, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()