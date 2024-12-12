class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        card_inx = defaultdict(int)
        min_len = n + 1
        for i, card in enumerate(cards):
            if card in card_inx:
                min_len = min(min_len, i - card_inx[card] + 1)
            card_inx[card] = i
        return min_len if min_len < n + 1 else -1
