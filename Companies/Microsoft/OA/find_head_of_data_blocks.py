'''
given a list of datablocks, return the head of the datablocks

input [db4, db3, db2, db1]
db1 -> db2
db3 -> db4

return [db1, db3]
'''
class Datablock:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class FindAllHeads:
    def find_all_heads(self, input_list: list[Datablock]) -> list[Datablock]:
        visited = set()
        res = set()
        for db in input_list:
            if db not in visited:
                new_head = db
                while db:
                    if db in visited:
                        res.remove(db)
                        res.add(new_head)
                        break
                    visited.add(db)
                    db = db.next
                if not db: # if db is None
                    res.add(new_head)
        return list(res)

db1 = Datablock(1)
db2 = Datablock(2)
db3 = Datablock(3)
db4 = Datablock(4)
db1.next = db2
db3.next = db4
s = FindAllHeads()
res = s.find_all_heads([db4, db3, db2, db1])
for e in res:
    print(e.val)