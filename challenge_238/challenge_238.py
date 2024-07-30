from typing import List


class Solution:
    # Attempted Solution 1
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     product_list = []
    #     index_to_pop = 0
    #     num_list_counter = 0

    #     while index_to_pop <= len(nums) - 1:
    #         product_result = 1
    #         nums_copy = nums.copy()
    #         nums_copy.pop(index_to_pop)
    #         for n in nums_copy:
    #             product_result = product_result * n
    #         product_list.append(product_result)
    #         index_to_pop +=1


            
    #     return product_list

    # Attempted Solution 2
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     product_list = []

    #     index_to_swap = 1

    #     while True:
    #         product_result = 1
    #         if index_to_swap > len(nums):
    #             break
            
    #         for i in range(1, len(nums)):
    #             product_result = product_result * nums[i]

    #         product_list.append(product_result)  

    #         if index_to_swap <= len(nums) - 1:
    #             temp_val = nums[index_to_swap]
    #             nums[index_to_swap] = nums[0]
    #             nums[0] = temp_val

    #         index_to_swap = index_to_swap + 1

    #     return product_list

    # Attempted Solution 3 - Time Exceeded
    # class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     product = []
        
    #     for i in range(len(nums)):
    #         right_product = 1
    #         left_product = 1
    #         temp_product = 1

    #         # calculate right side product
    #         for j in range(i + 1, len(nums)):
    #             right_product *= nums[j]

    #         if i > 0:
    #             # calculate left side product
    #             for k in range(0, i):
    #                 left_product *= nums[k]
            
    #         temp_product = left_product * right_product
    #         product.append(temp_product)
        
    #     return product

    # Actual Solution
    """
    [-1, 1, 0, -3, 3]
      0, 1, 2,  3, 4

    LEFT PRODUCT:
    [-1]
    left_product = 1
    product_list = [1]

    [1]
    left_product = -1
    product_list = [1, -1]

    [0]
    left_product = -1
    product_list = [1, -1, -1]

    [-3]
    left_product = 0
    product_list = [1, -1, -1, 0]

    [3]
    left_product = 0
    product_list = [1, -1, -1, 0, 0]

    RIGHT PRODUCT:
    [-1]
    product_list = [1, -1, -1, 0, 0]
    right_product = 3

    [1]
    product_list = [1, -1, -1, 0, 0]
    right_product = -9

    [0]
    product_list = [1, -1, 9, 0, 0]
    right_product = 0

    [-3]
    product_list = [1, 0, 9, 0, 0]
    right_product = 0

    [3]
    product_list = [0, 0, 9, 0, 0]
    right_product = 0

    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = [1] * len(nums)
        left_product = 1
        right_product = 1

        for i in range(len(nums)):
            if i > 0:
                left_product = left_product * nums[i - 1]
            product_list[i] = left_product
        
        for i in range(len(nums) - 1, -1, -1):
            product_list[i] = product_list[i] * right_product
            right_product = right_product * nums[i]

        return product_list