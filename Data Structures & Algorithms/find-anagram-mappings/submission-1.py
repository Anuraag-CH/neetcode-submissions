class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        dict_nums2 = {}

        for i in range(0, len(nums2)):
            dict_nums2[nums2[i]] = i

        for i in range(0, len(nums1)):
            # check nums1 digit in nums2 dict

            nums1[i] = dict_nums2[nums1[i]]

        return nums1
