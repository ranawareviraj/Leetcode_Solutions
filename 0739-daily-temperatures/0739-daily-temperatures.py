class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperatures[index]:
                prev_temp_index = stack.pop()
                result[prev_temp_index] = index - prev_temp_index
            stack.append(index)
        
        return result