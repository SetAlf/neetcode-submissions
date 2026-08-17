class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}                                # hash map that contains frequency of each 
                                                  # number in list       
        
        freq = [[] for i in range(len(nums) + 1)] # freq array is created; freq[i] stores 
                                                  # all the numbers that appear i times
                                                  # array is size of len(nums) + 1 since 
                                                  # len(nums) is the max possible frequency 
                                                  # in nums list
        for num in nums:                          # iterate through nums list
            count[num] = 1 + count.get(num, 0)    # returns current count of num in nums list 
                                                  # returns 0 if num not found
                                                  # updates count by incrementing by 1

        for num, cnt, in count.items():           # iterate through count list 
            freq[cnt].append(num)                 # appends num to freq array at index cnt
                                                  # to put number in index that is the same
                                                  # value as the frequency of that number

        res = []                                  # res array created to return k most frequent elements 
        for i in range(len(freq) -1, 0, -1):      # for loop starts i at highest frequency down to 1
            for num in freq[i]:                   # starts at num with highest frequency
                res.append(num)                   # appends num with highest frequency first to list
                if len(res) == k:                 # if length of res array == k (There are k number of nums)
                    return res                    # res array is returned with k most frequent elements



