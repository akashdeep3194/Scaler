import sys
from datetime import timezone, datetime


class LRUCache:
    def __init__(self, capacity):
        self.dc = dict()
        self.capacity = capacity

    def get(self, key):
        ans = self.dc.get(key, -1)
        if ans == -1:
            return ans
        else:
            ans = self.dc[key][0]
            self.dc[key][1] = datetime.timestamp(datetime.now(timezone.utc))
        return ans

    def set(self, key, value):
        if self.capacity > len(self.dc):
            self.dc[key] = [value, datetime.timestamp(
                datetime.now(timezone.utc))]
        else:
            if self.dc.get(key, -1) != -1:
                self.dc[key] = [value, datetime.timestamp(
                    datetime.now(timezone.utc))]
                return
            mn = datetime.timestamp(datetime.now(timezone.utc))
            for k, v in self.dc.items():
                ts = v[1]
                if mn > ts:
                    mn = ts
                    del_key = k
            self.dc.pop(del_key)
            self.dc[key] = [value, datetime.timestamp(
                datetime.now(timezone.utc))]


if __name__ == "__main__":
    # 2 G 2 S 2 6 G 1 S 1 5 S 1 2 G 1 G 2
    arr = list(sys.stdin.readline().strip().split())
    s = LRUCache(int(arr[0]))
    arr = arr[1:]
    i = 0
    while i < len(arr):
        if arr[i] == "G":
            print(s.get(arr[i+1]))
            i += 2
        elif arr[i] == "S":
            s.set(arr[i+1], int(arr[i+2]))
            i += 3
