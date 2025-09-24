# LRU Cache
# https://www.geeksforgeeks.org/problems/lru-cache/1



from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def processQueries(cap, Q, Queries):
    lru = LRUCache(cap)
    result = []
    for query in Queries:
        if query[0] == "PUT":
            _, x, y = query
            lru.put(x, y)
        elif query[0] == "GET":
            _, x = query
            result.append(lru.get(x))
    return result


cap = 2
Q = 2
Queries = [["PUT", 1, 2], ["GET", 1]]
print(processQueries(cap, Q, Queries)) 

cap = 2
Q = 8
Queries = [["PUT", 1, 2], ["PUT", 2, 3], ["PUT", 1, 5], 
           ["PUT", 4, 5], ["PUT", 6, 7], ["GET", 4], 
           ["PUT", 1, 2], ["GET", 3]]
print(processQueries(cap, Q, Queries))  
