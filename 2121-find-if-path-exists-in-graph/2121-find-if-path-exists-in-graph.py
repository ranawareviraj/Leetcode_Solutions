class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(graph, source, destination, visited ):
            if source == destination:
                return True
            
            visited.add(source)
            for neighbor in graph[source]:
                if neighbor not in visited and dfs(graph, neighbor, destination, visited):
                    return True
            
            return False
        
        graph = defaultdict(list)
        for (x, y) in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        return dfs(graph, source, destination, visited )