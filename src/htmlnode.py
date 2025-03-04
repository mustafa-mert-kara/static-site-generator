


class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props
    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        html_text=" "
        for val in self.props:
            html_text+=f'{val}="{self.props[val]}" '
        return html_text[:-1]
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value == None:
            raise ValueError("No Value Detected")
        if self.tag==None or self.tag=="":
            return self.value
        if self.props is not None:
            prop_text=self.props_to_html()
            return f"<{self.tag}{prop_text}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag==None:
            raise ValueError("No Tag Detected")
        if self.children==None or len(self.children)==0:
            raise ValueError("No Children")
        html_text=f"<{self.tag}>"
        for child in self.children:
            html_text+=child.to_html()
        html_text+=f"</{self.tag}>"
        return html_text