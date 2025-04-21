# LeetCode 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # len(list1) == m + n
        # list1[m:] are zeros of size n
        
        if n == 0: # if nums2 is empty, no need to do anything
            pass
        if m == 0: # if nums1 is empty, just copy nums2 to nums1, nums1 = nums2 could not be applied
            for m in range(n - 1, -1, -1):
                nums1[m] = nums2.pop()
        else:
            while n > 0 and m + n > 0: # we do not want to use extra variable memory
                if m - 1 < 0 or nums1[m - 1] <= nums2[-1]:
                    nums1[m + n - 1] = nums2.pop() # go through nums2 until they are empty
                    n -= 1
                else:
                    nums1[m + n - 1] = nums1[m - 1]
                    m -= 1
        
        # It would be interesting to see if the algebra could be reduced without using a new variable, as we could theoretically save at least one cpu tick for each calculation

        # output result
        print(nums1)

# Test cases
print("LeetCode 88. Merge Sorted Array")
print("-------------------------------")
print("Testcases input (nums1, m, nums2, n) and output:")
print([1,2,3,0,0,0],3,[2,5,6],3)
merge([1,2,3,0,0,0],3,[2,5,6],3)
print([2,0],1,[1],1)
merge([2,0],1,[1],1)
print([4,5,6,0,0,0], 3, [1,2,3], 3)
merge([4,5,6,0,0,0], 3, [1,2,3], 3)
print([0],0,[1],1)
merge([0],0,[1],1)
print([4,0,0,0,0,0],1,[1,2,3,5,6],5)
merge([4,0,0,0,0,0],1,[1,2,3,5,6],5)
print([1,2,4,5,6,0],5,[3],1)
merge([1,2,4,5,6,0],5,[3],1)
print([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3)
merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3)
print([0,0,3,0,0,0,0,0,0],3,[-1,1,1,1,2,3],6)
merge([0,0,3,0,0,0,0,0,0],3,[-1,1,1,1,2,3],6)
print([0,2,0,0,0,0,0,0], 2, [-1,1,1,2,2,3], 6)
merge([0,2,0,0,0,0,0,0], 2, [-1,1,1,2,2,3], 6)