# 5052

# Trie 만들기

import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for letter in word:
            if (letter not in node.children):
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isEnd = True
    
    def isPrefix(self, word):
        node = self.root
        for letter in word:
            if (letter not in node.children):
                return False
            if (node.isEnd == True):
                return True
            node = node.children[letter]
        return False
    
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        trie = Trie()

        n = int(sys.stdin.readline())
        phones = [sys.stdin.readline().rstrip() for _ in range(n)]
        for phone in phones:
            trie.insert(phone)

        hasPrefix = False
        for phone in phones:
            hasPrefix = hasPrefix or trie.isPrefix(phone)
        
        if (hasPrefix):
            print("NO")
        else:
            print("YES")
        

if (__name__ == "__main__"):
    main()
