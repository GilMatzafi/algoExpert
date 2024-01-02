#O(n^2) time solution:

def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        for j in range(i + 1,len(array)-1):
            if array[j + 1] + array[i] == targetSum:
                return [array[i],array[j + 1]]
            
    return []

print(twoNumberSum([3,5,-4,8,11,1,-1,6],10))
        
        
    
    
    

