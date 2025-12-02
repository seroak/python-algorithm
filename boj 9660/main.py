class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        result = {}
        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in result:
                return result[(i, j)]
            if (i + j) % 2 == 1:  # 선택가능한 piles의 첫+끝 index를 더한게 홀수면 Alex차례
                result[(i, j)] = max(piles[i] + dp(i+1, j), piles[j] + dp(i, j-1))
                return result[(i, j)]
            else:  #Lee차례
                result[(i, j)] = max(-piles[i] + dp(i+1, j), -piles[j] + dp(i, j-1))
                return result[(i, j)]
        return dp(0, len(piles)-1) > 0  #Alex점수는 +하고 Lee점수는 -해서 반환한 가장 큰 점수가 0보다 크면 알렉스 이김