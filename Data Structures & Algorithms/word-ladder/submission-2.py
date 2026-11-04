from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
            
        # Ensure beginWord is accounted for
        if beginWord not in wordList:
            wordList.append(beginWord)
            
        L = len(beginWord)
        
        # Step 1: Pre-process words into wildcard pattern buckets (e.g., "hot" -> "*ot", "h*t", "ho*")
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                intermediate_word = word[:i] + "*" + word[i+1:]
                all_combo_dict[intermediate_word].append(word)
                
        # Step 2: Standard BFS queue tracking (word, current_transformation_steps)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            if current_word == endWord:
                return level
                
            # Check all possible 1-character mutations via wildcard patterns
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                
                for neighbor in all_combo_dict[intermediate_word]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                
                # Clear visited patterns to prevent redundant re-processing
                all_combo_dict[intermediate_word] = []
                
        return 0