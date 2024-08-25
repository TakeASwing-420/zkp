class Node:
  def __init__(self):
      self.chars = [None] * 26  # Array for 26 lowercase letters
      self.isending = False  # Flag to indicate the end of a word

class Trie:
  def __init__(self):
      self.root = Node()

  @staticmethod
  def index_finder(c):
      return ord(c) - ord('a')

  def insert(self, word: str) -> None:
      cur = self.root
      for c in word:
          index = self.index_finder(c)
          if cur.chars[index] is None:
              cur.chars[index] = Node()
          cur = cur.chars[index]  # Move down the trie
      cur.isending = True  # Mark the end of the word

  def search(self, word: str) -> bool:
      cur = self.root
      for c in word:
          index = self.index_finder(c)
          if cur.chars[index] is None:
              return False  # If the character isn't found, the word isn't present
          cur = cur.chars[index]
      return cur.isending  # Return whether it's the end of a valid word

  def startsWith(self, prefix: str) -> bool:
      cur = self.root
      for c in prefix:
          index = self.index_finder(c)
          if cur.chars[index] is None:
              return False  # If the character isn't found, the prefix isn't present
          cur = cur.chars[index]
      return True  # If we reach here, the prefix exists in the trie

# Example usage:
# obj = Trie()
# obj.insert("apple")
# print(obj.search("apple"))  # Returns True
# print(obj.search("app"))    # Returns False
# print(obj.startsWith("app"))  # Returns True
