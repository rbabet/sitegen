from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            splits = node.text.split(delimiter)
            if len(splits) % 2 == 0:
                raise Exception ("invalid Markdown syntax")
            elif len(splits) == 1:
                result.append(node)
            else:
                result.append(TextNode(splits[0], TextType.TEXT))
                result.append(TextNode(splits[1], text_type))
                result.append(TextNode(splits[2], TextType.TEXT))
    return result
