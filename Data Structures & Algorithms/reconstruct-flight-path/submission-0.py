class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}

        for t in tickets:
            source, dest = t

            if source not in adj:
                adj[source] = []
            adj[source].append(dest)
        
        for v in adj.values():
            v.sort()
            v.reverse()

        route = []

        def dfs(port):
            while adj.get(port, []):
                next_dest = adj[port].pop()
                dfs(next_dest)
            route.append(port)
        
        dfs('JFK')

        route.reverse()
        return route
