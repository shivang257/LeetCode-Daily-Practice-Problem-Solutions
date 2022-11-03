class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
    	
    	### count the frequency of each word in words
        counter = Counter(words)
        
        ### initialize res and mid. 
        ### mid represent if result is in case1 (mid=1) or case2 (mid=0)
        res = mid = 0 

        for word in counter.keys():
            
            if word[0]==word[1]:
            	### increase the result by the word frequency
                res += counter[word] if counter[word]%2==0 else counter[word]-1
                ### set mid to 1 if frequency is odd (using bit-wise OR to make it short)
                mid |= counter[word]%2
            
            elif word[::-1] in counter:
            	### increase the result by the minimum frequency of the word and its reverse
            	### we do not do *2 because we will see its reverse later
                res += min(counter[word],counter[word[::-1]])
        
        ### since we only count the frequency of the selected word
        ### times 2 to get the length of the palindrome
        return (res + mid) * 2