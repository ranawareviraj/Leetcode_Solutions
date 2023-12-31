class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_graph = defaultdict(list)
        prerequisites_count = [0] * numCourses

        for x, y in prerequisites:
            prerequisites_graph[y].append(x)
            prerequisites_count[x] += 1

        queue = deque()
        for course in range(numCourses):
            if prerequisites_count[course] == 0:
                queue.append(course)

        courses_completed = set()
        while queue:
            course = queue.popleft()
            courses_completed.add(course)

            for next_course in prerequisites_graph[course]:
                prerequisites_count[next_course] -= 1
                if prerequisites_count[next_course] == 0:
                    queue.append(next_course)

        return len(courses_completed) == numCourses
