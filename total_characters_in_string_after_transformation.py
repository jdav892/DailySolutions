class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def get_transformation_matrix(nums):
            T = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for step in range(1, nums[i] + 1):
                    T[i][(i + step) % 26] += 1
            return T
        
        def matrix_mult(A, B):
            result = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            return result

        def matrix_pow(matrix, power):
            result = [[int(i == j) for j in range(26)] for i in range(26)]
            while power:
                if power % 2:
                    result = matrix_mult(result, matrix)
                matrix = matrix_mult(matrix, matrix)
                power //= 2
            return result
        T = get_transformation_matrix(nums)
        T_power = matrix_pow(T, t)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        result = 0
        for i in range(26):
            for j in range(26):
                result = (result + count[i] * T_power[i][j]) % MOD 
        return result