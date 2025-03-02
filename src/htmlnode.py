


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
        if self.value == None or self.value =="":
            raise ValueError("No Value Detected")
        if self.tag==None or self.tag=="":
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
