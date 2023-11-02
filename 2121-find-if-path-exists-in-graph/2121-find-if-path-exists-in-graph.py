class UnionFind:
    def __init__(self, n):
        self.roots = list( range(n) )
        self.rank = [ 1 ] * n

    def find(self, node):
        if self.roots[node] != node:
            self.roots[node] = self.find(self.roots[node])
        return self.roots[node]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            # Modify the root of the smaller group as the root of the
            if self.rank[ root_x ] > self.rank[ root_y ]:
                root_x, root_y = root_y, root_x

            # larger group, also increment the size of the larger group.
            self.rank[ root_y ] += self.rank[ root_x ]
            self.roots[ root_x ] = root_y

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        union_find = UnionFind(n)
        # Make union of all edges
        for x, y in edges:
            union_find.union(x, y)

        # Use find function to check if both source and destination belogs to same group
        return union_find.find(source) == union_find.find(destination)