class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0

        for i in range(len(operations)):
            match operations[i]:
                case "--X":
                    count -= 1
                case "X--":
                    count -= 1
                case "++X":
                    count += 1
                case "X++":
                    count += 1
                case _:
                    return 0
        return count