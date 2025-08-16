class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        result = []

        for i in range(len(str_num)):
            result.append(str_num[i])
            
        for i in range(len(result)):
            if result[i] == "6":
                result[i] = "9"
                break
            
        return int("".join(result))