class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        greatest_element = -1
        for i in range(len(arr) - 1, -1, -1):
            current_element = arr[i]
            arr[i] = greatest_element
            greatest_element = max(greatest_element, current_element)

        return arr
