class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.data_store.get(key):
            self.data_store[key] = []
            self.data_store[key].append([timestamp,value])
        else:
            self.data_store[key].insert(0,[timestamp,value])
        # import pdb; pdb.set_trace()
        

    def get(self, key: str, timestamp: int) -> str:
        store_list = self.data_store.get(key,[])
        if len(store_list) == 0:
            return ""
        for data in store_list:
            if data[0] <= timestamp:
                return data[1]
        return ""

        
ops = ["set","set","get","get","get","get","get"]
inputs  = [["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
obj = TimeMap()
for x,y in zip(ops,inputs):
    if x == "set":
        obj.set(y[0],y[1],y[2])
    else:
        print(obj.get(y[0],y[1]))
    
    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)