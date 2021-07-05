# LRU(least recent used) Cache
from collections import OrderedDict
class lru_cache():
    def __init__(self,k):
        self.lru=OrderedDict()
        self.k=k
    def put(self,key,val):
        self.lru[key] = val
        if len(self.lru)>self.k:
            self.lru.popitem(last=False)
    def get(self,key):
        if key not in self.lru:
            return -1
        else:
            self.lru.move_to_end(key)
        return self.lru[key]
    def print_all(self):
        return self.lru
a=lru_cache(3)
a.put(1,'x')
a.put(2,'y')
a.put(3,'z')
print(a.print_all())
a.put(4,'k')
print(a.get(3))
a.put(5,'v')
a.put(1,'x')
print(a.print_all())
