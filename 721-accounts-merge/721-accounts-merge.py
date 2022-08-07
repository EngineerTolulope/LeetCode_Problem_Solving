class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            
            # build edge for all emails
            email_1 = account[1]
            email_to_name[email_1] = name
            for email_2 in account[2:]:
                graph[email_1].add(email_2) # won't add the same email twice since it's a set
                graph[email_2].add(email_1)
                email_to_name[email_2] = name
                
        result = []
        visited = set()
        for email in email_to_name:
            if email not in visited:
                stack = [email]
                visited.add(email)
                emails = []
                
                while stack:
                    current = stack.pop()
                    emails.append(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            visited.add(neighbor)
                result.append([email_to_name[email]] + sorted(emails))
        return result