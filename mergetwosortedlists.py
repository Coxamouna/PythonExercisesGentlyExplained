# You could write this function in one line of code by using Python’s 
# sorted() function: 
# return sorted(list1 + list2)
# 
# This would defeat the purpose of the exercise, so don’t use the 
# sorted() function or sort() method as part of your solution.
# The lists of numbers passed for these parameters are already in sorted
# order from smallest to largest number:

def mergeTwoLists(list1, list2):
    mergedList = []
    # special case: one or both empty
    if len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    else:
        i = 0
        j = 0
        while (i < len(list1) and j < len(list2)):
            # if the numbers are equal, they are both added to the merged list and we are incrementing both indices:
            if list1[i] == list2[j]:
                mergedList.append(list1[i])
                mergedList.append(list2[j])
                i += 1
                j += 1
            # else, if the number from list 1 is smaller than the number from list 2, then we are apppending the smallest one
            # to the list and incrementing the index for the first list:
            elif list1[i] < list2[j]:
                mergedList.append(list1[i])
                i += 1
            # else, if the number from list 2 is smaller than the number from list 1, then we are appending the smallest one
            # to the list and incrementing the index in the second list:
            else:
                mergedList.append(list2[j])
                j += 1
        
        # one list ends sooners than the other - just append the rest of the longer one as the lists is already sorted
        if i == len(list1):
            while j < len(list2):
                mergedList.append(list2[j])
                j += 1
        
        if j == len(list2):
            while i < len(list1):
                mergedList.append(list1[i])
                i += 1        
        
        return mergedList

assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]