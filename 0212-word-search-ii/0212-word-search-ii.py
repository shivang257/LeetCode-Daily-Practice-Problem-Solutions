class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        #make trie
        count = Counter()
        for l in board:
            count += Counter(l)
        trie={}
        for w in words:
            wc = Counter(w)
            for c in wc:
				# optimization, ignore word if there isn't enough c in board
                if wc[c] > count[c]:
                    continue
            t=trie
            for c in w:
                if c not in t:
                    t[c]={}
                t=t[c]
            t['#']='#'
        self.res=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board,i,j,trie,[])
        return self.res
    
    def find(self,board,i,j,trie,pre):
        if '#' in trie:
			# optimization, delete for avoiding duplicated matches
            del trie["#"]
            self.res.append(''.join(pre))
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return
        if board[i][j] in trie:
            tmp = board[i][j]
            board[i][j] = '$'
            pre.append(tmp)
            self.find(board,i+1,j,trie[tmp],pre)
            self.find(board,i,j+1,trie[tmp],pre)
            self.find(board,i-1,j,trie[tmp],pre)
            self.find(board,i,j-1,trie[tmp],pre)
            board[i][j] = tmp
            pre.pop()
            if not trie[board[i][j]]:
				# nothing in trie[board[i][j]] because of matched before, delete node for optimization
                del trie[board[i][j]]