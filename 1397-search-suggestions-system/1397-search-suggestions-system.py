class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.suggestions = []

    def build_trie(self, products):
        root = self.TrieNode()
        for product in products:
            node = root
            for ch in product:
                if ch not in node.children:
                    node.children[ch] = self.TrieNode()
                node = node.children[ch]

                node.suggestions.append(product)
                node.suggestions.sort()
                if len(node.suggestions) > 3:
                    node.suggestions.pop()

        return root

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie().build_trie(products)
        ans = []
        node = trie

        for ch in searchWord:
            if ch in node.children:
                node = node.children[ch]
                ans.append(node.suggestions)
            else:
                # deadend reached
                node.children = {}
                ans.append([])

        return ans
