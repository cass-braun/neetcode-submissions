class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
            
        # Queue stores: (current_cost, current_node, stops_made)
        q = deque([(0, src, 0)])
        
        # Track the minimum cost to reach a node with a specific number of stops
        # To avoid TLE, we can store min costs. An array of min prices initialized to infinity.
        min_costs = [float('inf')] * n
        
        ans = float('inf')
        stops = 0
        
        while q and stops <= k + 1:
            # Process level by level (each level represents 1 flight/stop)
            for _ in range(len(q)):
                cost, node, steps = q.popleft()
                
                if node == dst:
                    ans = min(ans, cost)
                    continue
                    
                for neighbor, price in adj[node]:
                    next_cost = cost + price
                    # Only proceed if the new cost is better than what we've seen 
                    # AND we haven't exceeded our stop limit
                    if next_cost < min_costs[neighbor]:
                        min_costs[neighbor] = next_cost
                        q.append((next_cost, neighbor, steps + 1))
            stops += 1
            
        return ans if ans != float('inf') else -1