class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build prerequisites graph and counter of number of prerequisites
        graph = defaultdict(list)
        no_of_prerequisites = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            no_of_prerequisites[course] += 1
        
        # BFS Queue
        queue = deque([]) 

        # Add all level 0 onto queue -
        # i.e all courses without pre-requisites
        for course, prerequisite_count in enumerate(no_of_prerequisites):
            if prerequisite_count == 0:
                queue.append(course)
        
        # List to track course order
        course_order = []
        while queue:
            # Process all courses without pre-requisites
            level = len(queue)
            for _ in range(level):
                course = queue.popleft()
                course_order.append(course)

                for next_course in graph[course]:
                    no_of_prerequisites[next_course] -= 1
                    # Add all next_courses whos prerequisites are completed
                    if no_of_prerequisites[next_course] == 0:
                        queue.append(next_course)

        # If it is impossible to finish all courses, return an empty array. 
        return course_order if len(course_order) == numCourses else []
