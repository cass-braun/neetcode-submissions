from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_name = {}
        graph = defaultdict(set)
        
        # 1. Build the graph and email-to-name mapping
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                graph[first_email].add(email)
                graph[email].add(first_email)
                
        # 2. Traverse the graph to find connected components
        visited = set()
        res = []
        
        for email in email_to_name:
            if email not in visited:
                # Perform DFS/BFS to collect all connected emails
                stack = [email]
                visited.add(email)
                current_emails = []
                
                while stack:
                    curr = stack.pop()
                    current_emails.append(curr)
                    
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                            
                # Sort emails, prepend name, and add to result
                current_emails.sort()
                res.append([email_to_name[email]] + current_emails)
                
        return res