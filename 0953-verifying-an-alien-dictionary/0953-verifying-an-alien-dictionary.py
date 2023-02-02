class Solution:
    def isAlienSorted(self, words, order):
        return words == sorted(words, key=lambda w: map(order.index, w))