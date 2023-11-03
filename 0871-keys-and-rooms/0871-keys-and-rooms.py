class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # BFS
        def bfs(start):
            # Set to track visited rooms
            visited_rooms = {start}
            queue = collections.deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in rooms[node]:
                    if neighbor not in visited_rooms:
                        visited_rooms.add(neighbor)
                        # Add neighbor to BFS queue
                        queue.append(neighbor)
            return len(visited_rooms)

        # Return if we visited all rooms
        return bfs(0) == len(rooms)
