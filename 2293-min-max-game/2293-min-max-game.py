class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        arr = [x for x in nums]
        n = len(arr)

        while n > 1:
            is_min = True
            n //= 2
            next_arr = [0] * n
            j = 0

            for i in range(n):
                if is_min:
                    next_arr[i] = min(arr[j], arr[j + 1]) 
                else:
                    next_arr[i] = max(arr[j], arr[j + 1]) 
                is_min = not is_min
                j += 2
                
            arr = next_arr

        return arr[0]
