class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        total_fruits = 0
        left = 0
        n = len(fruits)
        fruit_types = defaultdict(int)

        for right, right_fruit in enumerate(fruits):
            fruit_types[right_fruit] += 1

            while len(fruit_types) > 2:
                left_fruit = fruits[left]
                left += 1
                
                fruit_types[left_fruit] -= 1
                if fruit_types[left_fruit] == 0:
                    del fruit_types[left_fruit]
            
            total_fruits = max(total_fruits, right - left + 1)
        
        return total_fruits