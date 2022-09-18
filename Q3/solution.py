# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
class Solution:
    def getMedian(self, lst1, lst2, n, m) :
    
        i = 0 
        j = 0
        my_list = []
        for count in range(n+m) :
            if(i != n and j != m) :
                if lst1[i] > lst2[j] :
                    my_list.append(lst2[j])
                    j += 1
                else :
                    my_list.append(lst1[i])
                    i += 1           
            elif(i < n) :       
                my_list.append(lst1[i])
                i += 1       
                # for case when j<m,
            else :
                my_list.append(lst2[j])
                j += 1
        print("Merged List is :", my_list)
        size = len(my_list)
        if size % 2 == 1:
            median = my_list[size//2]
        else:
            median = (my_list[int(size/2)] + my_list[int(size/2)-1])/2

        return median

sol = Solution()      
list1 = [1,2]
list2 = [3,4]
len1 = len(list1)
len2 = len(list2)
median = sol.getMedian(list1, list2, len1, len2)
print("Median is :", median)
