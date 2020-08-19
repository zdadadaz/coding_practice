class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # if rowIndex==0:
        #     return [1]
        # if rowIndex==1:
        #     return [1, 1]
        # arr=[1, 1]
        # count = 2
        # while count <= rowIndex:
        #     tmparr = [1]
        #     for i in range(1,count):
        #         tmparr.append(arr[i-1]+arr[i])
        #     tmparr.append(1)
        #     arr = tmparr
        #     count+=1
        # return arr
        arr = [1]*(rowIndex+1)
        for i in range(1,rowIndex):
            for j in range(i,0,-1):
                arr[j] += arr[j-1]
        return arr
            