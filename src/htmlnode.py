class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
	
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is not None:
            complete = ""
            for key, value in self.props.items():
                complete = complete + " " + key + "=\"" + value + "\""
            return complete 
        return None

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError ("LeafNode requires value")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        if props_html is None:
            props_html = ""
        return "<" + self.tag + props_html + ">" + self.value + "</" + self.tag + ">"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError ("ParentNode requires tag")
        if self.children is None:
            raise ValueError ("ParentNode requires children")
        props_html = self.props_to_html()
        if props_html is None:
            props_html = ""
        complete = "<" + self.tag + props_html + ">"
        for child in self.children:
            complete = complete + child.to_html()
        complete = complete + "</" + self.tag + ">"
        return complete

