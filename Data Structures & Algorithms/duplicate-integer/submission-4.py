class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        watcher = set()
        for num in range(0,len(nums)):
            if nums[num] in watcher:
                return True
            watcher.add(nums[num])
        return False