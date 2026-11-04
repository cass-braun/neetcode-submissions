from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
            
        # If beginWord is not in wordList, add it so it can be part of the graph
        if beginWord not in wordList:
            wordList.append(beginWord)
            
        L = len(beginWord)
        
        # Step 1: Group words by their generalized wildcard patterns (e.g., "hot" -> "*ot", "h*t", "ho*")
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                intermediate_word = word[:i] + "*" + word[i+1:]
                all_combo_dict[intermediate_word].append(word)
                
        # Step 2: Perform BFS
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            if current_word == endWord:
                return level
                
            # Find all generic patterns for the current word
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                
                # Traverse all words that share this wildcard pattern
                for neighbor in all_combo_dict[intermediate_word]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                
                # Optimization: Clear the list so we don't re-visit these edges
                all_combo_dict[intermediate_word] = []
                
        return 0