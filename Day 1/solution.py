#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        max_item = -1
        second_largest = -2
        
        for item in arr:
            if item > max_item:
                second_largest = max_item
                max_item = item
            elif second_largest < item and item < max_item:
                second_largest = item

        return second_largest


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends