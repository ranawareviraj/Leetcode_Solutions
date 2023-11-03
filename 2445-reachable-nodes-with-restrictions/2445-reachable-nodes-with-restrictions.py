class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def dfs(node, seen):
            seen.add(node)
            count = 1

            for neighbor in graph[node]:
                if neighbor not in seen:
                    count += dfs(neighbor, seen)
            return count

        # Build graph
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set(restricted)
        return dfs(0, seen)
