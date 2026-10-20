class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(start, root):
            node = root
            for i in range(start, len(word)):
                c = word[i]
                if c == ".":
                    return any(dfs(i + 1, child) for child in node.children.values())
                    # for child in node.children.values():
                    #     if dfs(i + 1, child):
                    #         return True
                    # return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.is_end

        return dfs(0, self.root)
