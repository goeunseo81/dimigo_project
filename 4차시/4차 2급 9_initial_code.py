#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(height):
    #여기에 코드를 작성해주세요.
    count = 0
    '''
    for i in range(4):
        for j in range(4):
            nb=[]
            for n1,n2 in [[0,1],[0,-1],[1,0],[-1,0]]:
                ni,nj=i+n1,j+n2
                if 0<=ni<=3 and 0<=nj<=3:
                    nb.append(height[ni][nj])
            if min(nb)>height[i][j]:
                count+=1
    '''
    arr = [[max(max(row) for row in height)] * (len(height[0])+2) for _ in range(len(height[0])+2)]
    for i in range(len(height[0])):
        for j in range(len(height[0])):
            arr[i+1][j+1]=height[i][j]
    for i in range(1,len(height[0])+1):
        for j in range(1,len(height[0])+1):
            if min(arr[i][j],arr[i+1][j],arr[i-1][j],arr[i][j+1],arr[i][j-1])==arr[i][j]:
                count+=1
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")