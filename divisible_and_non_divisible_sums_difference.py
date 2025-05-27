class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        y = []
        no = []
        for num in range(1, n+1):
            if num % m != 0:
                y.append(num)
            else:
                no.append(num)
        return sum(y) - sum(no)