class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_set = {outgoing for outgoing, _ in paths}

        for outgoing, incoming in paths:
            if not incoming in outgoing_set:
                return incoming