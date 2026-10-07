class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}

        for num in nums:
            numFreq[num] = 1 + numFreq.get(num, 0)

        soln = []

        for num, cnt in numFreq.items():
            soln.append([cnt, num])
        soln.sort()

        sortSoln = []
        while len(sortSoln) < k:
            sortSoln.append(soln.pop()[1])
        return sortSoln       