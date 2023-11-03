class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        start_nodes = set()
        end_nodes = set()
        for start, end in edges:
            start_nodes.add(start)
            end_nodes.add(end)
        
        ans = []
        for node in start_nodes:
            if node not in end_nodes:
                ans.append(node)
        
        return ans