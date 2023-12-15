class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = set()

        for path in paths:
            src.add(path[0])

        for path in paths:
            dest = path[1]
            if dest not in src:
                return dest
        
        return ""
        
