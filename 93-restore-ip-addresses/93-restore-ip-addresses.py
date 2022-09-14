class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        
        result = []
        def backtracking(start, dot_count, current_ip):
            if start == len(s) and dot_count == 4:
                result.append(current_ip[:-1])
                return
            if dot_count > 4:
                return
            
            for end in range(start, min(start + 3, len(s))):
                substring = s[start:end+1]
                num = int(substring)
                
                if num <= 255 and (start == end or substring[0] != '0'):
                    backtracking(end + 1, dot_count + 1, current_ip + substring + '.')
        backtracking(0, 0, '')
        return result