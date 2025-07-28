def countNegatives(grid):
    count = 0
    index = -1
    for i in range (len(grid)):
        low = grid[i][0]
        high = grid[i][len(grid[i]) - 1]
        while (low <= high):
            mid = (low + high) // 2
            index = mid
            if (grid[i][mid] < 0):
                high = mid - 1
            else:
                low = mid + 1
        count = count + len(grid[i]) - index
    return count


print(countNegatives([[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] ))