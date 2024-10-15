class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        card_map = {}  
        min_length = float('inf') 
        # Iterate through the cards list
        for i, card in enumerate(cards):  
            if card in card_map:
                min_length = min(min_length, i - card_map[card] + 1)
            
            card_map[card] = i
        
       
        return min_length if min_length <= n else -1
