from typing import List


class Node:

    def __init__(self):
        self.children = {}
        self.isending = 0


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isending = 1


class Encrypter:

    def __init__(self, keys: List[str], values: List[str],
                 dictionary: List[str]):
        ordered_keys, ordered_values = {}, {}
        for key, value in zip(keys, values):
            ordered_keys[key] = value
            if value in ordered_values:
                ordered_values[value].append(key)
            else:
                ordered_values[value] = [key]
        self.keys = ordered_keys
        self.values = ordered_values
        self.trie = Trie()

        for valid in dictionary:
            self.trie.insert(valid)

    def encrypt(self, word1: str) -> str:
        res = ""
        for char in word1:
            if char in self.keys:
                res += self.keys[char]
            else:
                return ""
        return res

    def decrypt(self, word2: str) -> int:

        def solve(i: int, root: Node) -> int:
            if i == len(word2):
                return root.isending
            else:
                s = word2[i:i + 2]
                if s not in self.values:
                    return 0
                ans = 0
                for key in self.values[s]:
                    if key in root.children:
                        ans += solve(i + 2, root.children[key])
                return ans

        return solve(0, self.trie.root)


# Example usage:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
