class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_count = []
        for i, sticker in enumerate(stickers):
            sticker_count.append({})
            for char in sticker:
                sticker_count[i][char] = 1 + sticker_count[i].get(char, 0)
        
        dp = {} # key = subseq of target : value= min num of stickers
        def dfs(target, sticker):
            if target in dp:
                return dp[target]
            
            result = 1 if sticker else 0
            remain_target = ''
            for char in target:
                if char in sticker and sticker[char] >= 1:
                    sticker[char] -= 1
                else:
                    remain_target += char
            
            if remain_target:
                used = sys.maxsize
                for sticker_ in sticker_count:
                    if remain_target[0] not in sticker_:
                        continue
                    used = min(used, dfs(remain_target, sticker_.copy()))
                dp[remain_target] = used
                result += used
            return result
        
        result = dfs(target, {})
        return result if result != sys.maxsize else -1