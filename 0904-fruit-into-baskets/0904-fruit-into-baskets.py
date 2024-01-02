class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        total_fruits = 0
        left = 0
        n = len(fruits)
        basket = defaultdict(int)

        for right, fruit in enumerate(fruits):
            basket[fruit] += 1

            while len(basket) > 2:
                left_fruit = fruits[left]
                left += 1

                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
            
            total_fruits = max(total_fruits, right - left + 1)
        
        return total_fruits