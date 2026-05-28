class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for lst in matrix:
            n=len(lst)
            l=0
            r=n-1

            while l <= r:
                mid = (l + r) // 2

                if lst[mid] == target:
                    return True
                elif lst[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False