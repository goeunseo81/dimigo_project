def solution(arr):
    left, right = 0, len(arr)-1 # left 0 , right =-1번째
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1 # 1 ,3 /4 ,2 /2 ,1
        right -= 1 # 3 ,1/2, 4 /1, 2
    
    return arr # 3,2,4,1  left를 크게 하면  1,4,2,3그대로 출력
  

#The following is code to output testcase.
arr = [1, 4, 2, 3]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")