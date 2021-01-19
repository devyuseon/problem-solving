class MyHashMap:

    def __init__(self):
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value

    def get(self, key: int) -> int:
        if not key in self.dict:
            return -1
        else:
            return self.dict.get(key)

    def remove(self, key: int) -> None:
        if key in self.dict:
            del self.dict[key]

        # Your MyHashMap object wisll be instantiated and called as such:
        # obj = MyHashMap()
        # obj.put(key,value)
        # param_2 = obj.get(key)
        # obj.remove(key)
