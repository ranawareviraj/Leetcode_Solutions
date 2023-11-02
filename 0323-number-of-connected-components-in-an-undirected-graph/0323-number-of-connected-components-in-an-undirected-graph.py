class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build graph
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x) 
            
        # DFS starting from a node
        def dfs(node):
            # Base case : If node is already visited, its component is already explored
            # So just return
            if node in seen:
                return
            
            # If we come to this line means the node is being visited for the first time
            seen.add(node)

            # Recursively explore all the nodes part of current component
            for neighbor in graph[node]:
                dfs(neighbor)
        
        seen = set()
        number_of_components = 0

        # Visit all nodes in a graph in DFS manner
        for node in range(n):
            if node not in seen:
                number_of_components += 1
                dfs(node)

        return number_of_components
