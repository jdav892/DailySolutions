class FindElements:
    
    def __init__(self, root: Optional[TreeNode]):
        def recover(node, val):
            if not node:
                return
            self.values.add(val)
            
            if node.left:
                recover(node.left, 2 * val + 1)
            if node.right:
                recover(node.right, 2 * val + 2)
                
        self.values = set()
        recover(root, 0)
    
    def find(self, target: int) -> bool:
        return target in self.values