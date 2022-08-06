class TimeMap:
    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.storage:
            self.storage[key] = []
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.storage:
            return ''
        
        result = ''
        values = self.storage[key]
        left, right = 0, len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            middle_value = values[middle][0]
            middle_timestamp = values[middle][1]
            
            if middle_timestamp == timestamp:
                return middle_value
            elif middle_timestamp < timestamp:
                result = middle_value
                left = middle + 1
            else:
                right = middle - 1
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)