class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisites_graph = defaultdict(list)
        prerequisites_count = [0] * numCourses

        for x, y in prerequisites:
            prerequisites_graph[y].append(x)
            prerequisites_count[x] += 1

        queue = deque()
        for course in range(numCourses):
            if prerequisites_count[course] == 0:
                queue.append(course)

        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            for next_course in prerequisites_graph[course]:
                prerequisites_count[next_course] -= 1
                if prerequisites_count[next_course] == 0:
                    queue.append(next_course)

        return result if len(result) == numCourses else []