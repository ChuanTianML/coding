class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last, sum = 0, 0
        sum_set = set()
        for n in nums:
            last = sum
            if not 0 == k:
                sum %= k
            if n in sum_set:
                return True
            sum_set.add(last)
        return False