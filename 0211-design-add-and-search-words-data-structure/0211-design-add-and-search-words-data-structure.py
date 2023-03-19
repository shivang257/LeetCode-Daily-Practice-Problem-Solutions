class WordDictionary:

    def __init__(self):
        
        # Initialize your data structure here.
        self.children = [None]*26
        self.isEndOfWord = False
        

    def addWord(self, word: str) -> None:

        # Adds a word into the data structure.
        curr = self
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = WordDictionary()
            curr = curr.children[ord(c) - ord('a')]
        
        curr.isEndOfWord = True;
        

    def search(self, word: str) -> bool:

        # Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch != None and ch.search(word[i+1:]): return True
                return False
            
            if curr.children[ord(c) - ord('a')] == None: return False
            curr = curr.children[ord(c) - ord('a')]
        
        return curr != None and curr.isEndOfWord