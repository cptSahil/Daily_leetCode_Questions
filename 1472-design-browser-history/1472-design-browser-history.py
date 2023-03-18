class DLLNode:
    def __init__(self,url:str):
        self.data = url
        self.prev, self.next = None, None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.linked_list_head = DLLNode(homepage)
        self.current = self.linked_list_head
        

    def visit(self, url: str) -> None:
        new_node = DLLNode(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.data

    def forward(self, steps: int) -> str:
        while steps and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.data


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)