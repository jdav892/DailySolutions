class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = "".join(str(digit) for digit in digits)
        num_result = int(result)
        num_result += 1
        new_str = str(num_result)
        new_result = []
        for digit in new_str:
            new_result.append(int(digit))
        return new_result