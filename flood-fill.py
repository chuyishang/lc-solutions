class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = [(sr, sc)]
        visited = {(sr, sc)}
        while stack:
            print(stack)
            curr = stack[0]
            adj = [(curr[0],curr[1]-1), (curr[0]+1,curr[1]), 
                    (curr[0], curr[1]+1), (curr[0]-1, curr[1])]
            for tile in adj:
                if 0 <= tile[0] < len(image) and 0 <= tile[1] < len(image[0]):
                    if image[tile[0]][tile[1]] == image[curr[0]][curr[1]]:
                        if tile not in visited:
                            stack.append(tile)
                        visited.add(tile)
            stack.pop(0)
        for entry in visited:
            image[entry[0]][entry[1]] = color
        return image