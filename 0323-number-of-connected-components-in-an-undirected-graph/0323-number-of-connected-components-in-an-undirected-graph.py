class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build graph
        def build_graph(edges):
            graph = defaultdict(list)
            for (x, y) in edges:
                graph[x].append(y)
                graph[y].append(x)
            return graph

        def dfs(node, graph, visited):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor, graph, visited)
            
            return True

        graph = build_graph(edges)
        visited = set()
        count = 0

        for node in range(n):
            if dfs(node, graph, visited):
                count += 1
        
        return count