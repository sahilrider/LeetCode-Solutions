'''https://leetcode.com/problems/reveal-cards-in-increasing-order/'''

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        index = list(range(len(deck)))
        ans = [None]*len(deck)
        for card in sorted(deck):
            ans[index.pop(0)] = card
            if index:
                index.append(index.pop(0))
        return ans
        