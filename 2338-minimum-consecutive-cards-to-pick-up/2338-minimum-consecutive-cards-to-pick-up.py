class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        curr = 0
        min_cards = math.inf
        map = defaultdict(int)

        for right in range(len(cards)):
            map[cards[right]] += 1

            while map and len(map) < (right - left + 1):
                min_cards = min(min_cards, right - left + 1)
                map[cards[left]] -= 1
                if map[cards[left]] == 0:
                    map.pop(cards[left])
                left += 1
        
        return min_cards if min_cards != math.inf else -1

