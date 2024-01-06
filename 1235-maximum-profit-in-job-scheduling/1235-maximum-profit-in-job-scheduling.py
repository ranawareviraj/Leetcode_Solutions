class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        @cache
        def dfs(i):
            if i == len(intervals):
                return 0
            
            result = dfs(i + 1)

            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            
            result = max(result, intervals[i][2] + dfs(j))
            return result
        
        intervals = sorted(zip(startTime, endTime, profit))

        return dfs(0)