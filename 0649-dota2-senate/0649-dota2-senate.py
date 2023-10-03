class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate_list = list(senate)
        n = len(senate_list)
        radiant = []
        dire = []

        for i, senator in enumerate(senate_list):
            if senator == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.pop(0)
            dire.pop(0)

        return "Radiant" if radiant else "Dire"