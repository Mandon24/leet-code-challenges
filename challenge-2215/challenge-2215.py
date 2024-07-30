from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        ans0 = []
        ans1 = []

        for num in nums1:
            if num not in nums2 and num not in ans0:
                ans0.append(num)
        for num in nums2:
            if num not in nums1 and num not in ans1:
                ans1.append(num)

        res.append(ans0)
        res.append(ans1)
        return res


# HashMap Solution
        # mpp = defaultdict(int)
        # list1 = []
        # result = []

        # # Process arr2 and store in hashmap
        # for i in arr2:
        #     mpp[i] = 1

        # # Find elements in arr1 not in arr2
        # for i in arr1:
        #     if mpp[i] == 0:
        #         list1.append(i)
        #         mpp[i] = 1

        # result.append(list1)

        # # Reset list1 and hashmap
        # list1 = []
        # mpp = defaultdict(int)

        # # Process arr1 and store in hashmap
        # for i in arr1:
        #     mpp[i] = 1

        # # Find elements in arr2 not in arr1
        # for i in arr2:
        #     if mpp[i] == 0:
        #         list1.append(i)
        #         mpp[i] = 1

        # result.append(list1)

        # return result


# Set Solution
        # set1, set2 = set(nums1), set(nums2)
        # return [list(set1-set2), list(set2-set1)]
