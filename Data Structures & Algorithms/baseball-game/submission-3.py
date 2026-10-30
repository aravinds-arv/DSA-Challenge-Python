class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for x in operations:
            if x == "+":
                record.append(record[-1] + record[-2])
            elif x == "D":
                record.append(2 * record[-1])
            elif x == "C":
                record.pop()
            else:
                record.append(int(x))

        return sum(record)
