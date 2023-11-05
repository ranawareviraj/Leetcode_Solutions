class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def finish_order(course, pre_graph, course_status, current_order):
            if course_status[course] == IN_PROGRESS:
                return False
            if course_status[course] == COMPLETED:
                return True

            course_status[course] = IN_PROGRESS
            
            for pre_course in pre_graph[course]:
                if not finish_order(pre_course, pre_graph, course_status, current_order):
                    return False
                
            current_order.append(course)
            course_status[course] = COMPLETED
            return True

        pre_graph = defaultdict(list)
        for course, pre in prerequisites:
            pre_graph[pre].append(course)

        NOT_STARTED, IN_PROGRESS, COMPLETED = 0, 1, 2
        course_status = [NOT_STARTED] * numCourses

        order = []
        for course in range(numCourses):
            if not finish_order(course, pre_graph, course_status, order):
                return []

        return reversed(order)