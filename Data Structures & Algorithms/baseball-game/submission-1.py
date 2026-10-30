class Record:
    def __init__(self):
        self.stack = []

    def isempty(self):
        return self.stack == []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        return None

    def tsum(self):
        if not self.isempty():
            return sum(self.stack)
        return 0

    def __str__(self):
        return str(self.stack)

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = Record()

        for x in operations:
            try:
                record.push(int(x))
            except:
                if x == "+":
                    b = record.pop()
                    a = record.pop()
                    newScore = a + b
                    record.push(a)
                    record.push(b)
                    record.push(newScore)
                elif x == "D":
                    a = record.pop()
                    newScore = 2 * a
                    record.push(a)
                    record.push(newScore)
                else:
                    record.pop()

        return record.tsum()
