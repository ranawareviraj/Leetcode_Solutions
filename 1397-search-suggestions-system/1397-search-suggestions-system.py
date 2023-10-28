class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.suggestions = []

    # Build Trie for every product. 
    # Add top 3 suggestions at each node(prefix)
    def build_trie(self, products):
        root = self.TrieNode()
        for product in products:
            node = root
            for ch in product:
                if ch not in node.children:
                    # If current character is not in the Trie,
                    # Create and add a child Trie node
                    node.children[ch] = self.TrieNode()
                # Traverse to child the node
                node = node.children[ch]

                # This is where we can track additional data with the node - 
                # In our case, top 3 suggestions
                node.suggestions.append(product)

                # If there are more than 3 suggestions,
                # remove lexiographically larger suggestion
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
                # deadend reached - no further suggestions
                node.children = {}
                ans.append([])
                
        return ans
    