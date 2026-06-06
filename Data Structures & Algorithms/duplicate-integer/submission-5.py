import pandas as pd
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        df = pd.DataFrame(nums)
        dupes = df.duplicated().any()
        return bool(dupes)