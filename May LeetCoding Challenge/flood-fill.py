# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/

# Input: image: List[List[int]], sr: int, sc: int, newColor: int
# Output: List[List[int]]

def floodFill(image, sr, sc, newColor):
    prevColor = image[sr][sc]
    image[sr][sc] = newColor
    
    # If new color is already the color of starting pixel, then return
    if prevColor == newColor:
        return(image)

    else:
        # Moving 1 cell up
        if sr-1 >= 0 and image[sr-1][sc] == prevColor:
            floodFill(image, sr-1, sc, newColor)

        # Moving 1 cell left
        if sc-1 >= 0 and image[sr][sc-1] == prevColor:
            floodFill(image, sr, sc-1, newColor)

        # Moving 1 cell right
        if sc+1 < len(image[0]) and image[sr][sc+1] == prevColor:
            floodFill(image, sr, sc+1, newColor)

        # Moving 1 cell down
        if sr+1 < len(image) and image[sr+1][sc] == prevColor:
            floodFill(image, sr+1, sc, newColor)

        return(image)

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2))    # Output: [[2,2,2],[2,2,0],[2,0,1]]
'''
Image is represented as following, with the number at each cell denotes its color.
    0  1  2
0 [ 1  1  1 ]
1 [ 1  1  0 ]       Starting pixel is (1,1), whose color is 1
2 [ 1  0  1 ]

Cells to be floodfilled: (0,0), (0,1), (0,2), (1,0), (1,1), (2,0)
'''

print(floodFill([[1,2,1],[1,1,3],[1,4,1]], 2,0,2))    # Output: [[2,2,1],[2,2,3],[2,4,1]]
'''
Image is represented as following, with the number at each cell denotes its color.
    0  1  2
0 [ 1  2  1 ]
1 [ 1  1  3 ]       Starting pixel is (2,0), whose color is 1
2 [ 1  4  1 ]

Cells to be floodfilled: (0,0), (0,1), (1,0), (1,1), (2,0)
'''

print(floodFill([[0,0,0], [0,1,1]], 1,1,1))           # Output: [[0,0,0], [0,1,1]]
'''
Image is represented as following, with the number at each cell denotes its color.
    0  1  2
0 [ 0  0  0 ]
1 [ 0  1  1 ]       Starting pixel is (1,1), whose color is 1

Here the starting pixel already has same color as the newColor
This eans no change will occur due to floodfilling
Hence, returning original image list as it is.
'''