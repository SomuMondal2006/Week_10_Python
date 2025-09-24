# Minimum platforms required
# https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1



def minPlatforms(arr, dep):
    n = len(arr)

    arr.sort()
    dep.sort()
    
    plat_needed = 1
    max_plat = 1
    i = 1 
    j = 0  
    
    while i < n and j < n:
        if arr[i] <= dep[j]:
            plat_needed += 1
            i += 1
            max_plat = max(max_plat, plat_needed)
        else:
            plat_needed -= 1
            j += 1
    
    return max_plat

arr1 = [900, 940, 950, 1100, 1500, 1800]
dep1 = [910, 1200, 1120, 1130, 1900, 2000]
print(minPlatforms(arr1, dep1)) 

arr2 = [900, 1235, 1100]
dep2 = [1000, 1240, 1200]
print(minPlatforms(arr2, dep2))  

arr3 = [1000, 935, 1100]
dep3 = [1200, 1240, 1130]
print(minPlatforms(arr3, dep3))  
