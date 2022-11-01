class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def sorter(x, y):
            n, m = len(x), len(y)
            if n != m:
                return -1 if n < m else 1 # when n > m
            else:
                return -1 if x < y else 1 if x > y else 0
            
        key = cmp_to_key(sorter)
        nums.sort(key=key, reverse=True)
        return nums[k-1]