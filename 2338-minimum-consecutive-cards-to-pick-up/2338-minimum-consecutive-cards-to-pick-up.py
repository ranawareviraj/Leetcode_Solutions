class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        min_cards = math.inf
        map = defaultdict(int)

        for right, card in enumerate(cards):
            if card in map:
                left = map[card]
                min_cards = min(right - left + 1, min_cards)
            
            map[card] = right
            
        return min_cards if min_cards != math.inf else -1

