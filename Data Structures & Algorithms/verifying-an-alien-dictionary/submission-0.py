class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Create a mapping of each character to its index in the alien order
        order_map = {char: i for i, char in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # Compare characters of the adjacent words
            for j in range(min(len(word1), len(word2))):
                char1 = word1[j]
                char2 = word2[j]
                
                if char1 != char2:
                    # If characters differ, check their alien order
                    if order_map[char1] > order_map[char2]:
                        return False
                    break
            else:
                # If we finish the loop without breaking, it means one word is a prefix of the other.
                # If word1 is longer than word2, it's invalid (e.g., "apple" before "app").
                if len(word1) > len(word2):
                    return False
                    
        return True