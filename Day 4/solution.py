#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        arr_length = len(arr)
        if arr_length == 0 or arr_length == 1:
            return arr

        d = int(d%arr_length)
        
        arr = arr[d:]+arr[0:d]

        return arr

# Tast Cases
s = Solution()
print(s.rotateArr([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 3))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# import math


# def main():
#     T = int(input())

#     while (T > 0):
#         A = [int(x) for x in input().strip().split()]
#         nd = [int(x) for x in input().strip().split()]
#         D = nd[0]
#         ob = Solution()
#         ob.rotateArr(A, D)

#         for i in A:
#             print(i, end=" ")

#         print()

#         T -= 1

#         print("~")


# if __name__ == "__main__":
#     main()

# } Driver Code Ends