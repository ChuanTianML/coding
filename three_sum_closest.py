class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        maybes = []
        for i, n in enumerate(nums[:-2]):
            l, r = i+1, len(nums)-1
            lwst = n + nums[l] + nums[l+1]
            lgst = n + nums[r-1] + nums[r]
            if lgst < target:
                maybes.append(lgst)
            elif lwst > target:
                maybes.append(lwst)
            else:
                while l < r:
                    maybe = n + nums[l] + nums[r]
                    maybes.append(maybe)
                    if maybe < target: l += 1
                    elif maybe > target: r -= 1
                    else: return target
        maybes.sort(key=lambda x:abs(x-target))
        return maybes[0]
