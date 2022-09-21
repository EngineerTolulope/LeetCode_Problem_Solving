class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log, digit_log = [], []
        
        for log in logs:
            item = log.split(' ')
            if item[1].isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log.split())
        
        letter_log.sort(key=lambda x: x[0])
        letter_log.sort(key=lambda x: x[1:])
        letter_log = [' '.join(x) for x in letter_log]
        return letter_log + digit_log