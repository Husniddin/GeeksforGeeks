#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        i = 0
        j = 0
        while i < len(arr):
            if arr[i] == 0:
                if arr[j] != 0:
                    j = i
            elif arr[j] == 0:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1

            i += 1
    	
        return arr

s = Solution()
print(s.pushZerosToEnd([1, 0, 0, 2, 3, 0]))
print(s.pushZerosToEnd([10, 20, 30]))
print(s.pushZerosToEnd([0, 0]))
print(s.pushZerosToEnd([0]))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# if __name__ == '__main__':
#     tc = int(input())
#     while tc > 0:
#         arr = list(map(int, input().strip().split()))
#         ob = Solution()
#         ob.pushZerosToEnd(arr)
#         for x in arr:
#             print(x, end=" ")
#         print()
#         tc -= 1
# } Driver Code Ends