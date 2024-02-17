def furthestBuilding() -> int:
    heights = [4, 2, 7, 6, 9, 14, 12]
    bricks = 5
    ladders = 1
    furthest_building = 0
    for i in range(0, len(heights) - 1):
        if heights[i] >= heights[i + 1]:
            furthest_building = i + 1
        elif heights[i] < heights[i + 1]:
            if bricks > 0:
                bricks -= (heights[i + 1] - heights[i])
                heights[i] += (heights[i + 1] - heights[i])
            elif bricks == 0 or bricks != (heights[i + 1] - heights[i]):
                if ladders > 0:
                    ladders -= 1
                    heights[i] += (heights[i + 1] - heights[i])
                else:
                    furthest_building = i
                    break
    return furthest_building


print(furthestBuilding())