class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        a = self.data
        if key not in a:
            a[key] = [(value, timestamp)]
        else:
            a[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        r = ""
        if key in self.data:
            a = self.data[key]
        else:
            return r
        for i in a:
            if i[1] <= timestamp:
                r = i
        if isinstance(r, tuple):
            return r[0]
        return r

        
