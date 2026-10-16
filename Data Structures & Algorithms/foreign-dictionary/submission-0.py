class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        in_degree = {c: 0 for c in adj}

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            matched = False

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    matched = True
                    break
            if not matched and len(w1) > len(w2):
                return ""
                 
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)

            for neighbour in adj[curr]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(res) != len(adj):
            return ""

        return "".join(res)
