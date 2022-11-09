class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local = ''
            for i, char in enumerate(email):
                if char == '@' or char == '+':
                    break
                elif char == '.':
                    continue
                else:
                    local += char
        
            while email[i] != '@':
                i += 1
            domain = email[i+1:]
            unique_emails.add((local, domain))
            
        return len(unique_emails)