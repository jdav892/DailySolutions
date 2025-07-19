class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x: x.split("/"))

        def subfolder(a, b):
            if not a.startswith(b):
                return False

            ap = a.split("/")
            bp = b.split("/")
            if len(ap) < len(bp):
                return False

        
            for za, zb in zip(ap, bp):
                if za != zb:
                    return False

            else:
                return True

        
        stack = []
        for f in folder:
            stack.append(f)
            if len(stack) >= 2 and subfolder(stack[-1], stack[-2]):
                stack.pop()
        return stack