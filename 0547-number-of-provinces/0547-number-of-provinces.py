class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Helper function to build graph as ajancency list from Adjacency Matrix
        def build_graph(isConnected):
            graph = defaultdict(list)
            for i in range(n):
                for j in range(n):
                    if isConnected[i][j] == 1:
                        graph[i].append(j)
                        graph[j].append(i)
            return graph

        # Traverse graph using DFS starting at a given city
        def dfs(city, visited):
            visited.add(city)

            for neighbor_city in graph[city]:
                if neighbor_city not in visited:
                    dfs(neighbor_city, visited)
        
        
        n = len(isConnected)
        graph = build_graph(isConnected)
        visited = set()
        number_of_provinces = 0

        # For each city if we haven't explored its province yet, we found new province.
        # Start DFS from that city and mark all cities of that province as visited
        for city in graph:
            if city not in visited:
                dfs(city, visited)
                number_of_provinces += 1
        
        return number_of_provinces
