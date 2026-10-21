class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        res = []

        def backtrack(r, c, parent):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] not in parent.children:
                return False

            ch = board[r][c]
            node = parent.children[ch]
            if node.word:
                res.append(node.word)
                node.word = None

            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                backtrack(r + dr, c + dc, node)
            board[r][c] = ch

            if not node.children and not node.word:
                del parent.children[ch]

        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, trie.root)
        return res
