class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        stack = []

        for token in tokens:
            if token:
                if token == "..":
                    if stack:
                        stack.pop()
                elif token != ".":
                    stack.append(token)
        
        # Build simplified canonical path
        result = ["/"]
        for token in stack:
            result.append(token)
            result.append("/")
        if len(result) > 1:
            result.pop()

        return "".join(result)
        
