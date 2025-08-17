class pain_element:
    def two_Sum(self, nums, tar):
        lookup = {}

        for i, num in enumerate(nums):
            if tar - num in lookup:
                return [lookup[tar - num], i]
            lookup[num] = i

value = int(input("Enter sum for which you want to make this search : "))
print("index1=%d, index2=%d" % pain_element().two_Sum([10, 20, 30, 40, 50, 60, 70], value))