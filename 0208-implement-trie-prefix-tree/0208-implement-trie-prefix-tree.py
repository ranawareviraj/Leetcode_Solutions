class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_word = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                new_node = self.Node()
                node.children[ch] = new_node
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.traverse_trie(word)
        return False if not node else node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.traverse_trie(prefix)
        return True if node else False

    def traverse_trie(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node 
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)