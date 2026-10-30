class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for x in operations:
            try:
                record.append(int(x))
            except:
                if x == "+":
                    record.append(record[-1] + record[-2])
                elif x == "D":
                    record.append(2 * record[-1])
                else:
                    if len(record) > 0:
                        record.pop()

        return sum(record)
