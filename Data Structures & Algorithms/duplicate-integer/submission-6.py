import numpy as np
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = np.array(nums)
        dupes = len(np.unique(arr)) != len(arr)
        return dupes