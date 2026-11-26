class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if len(matrix) == 1:
            return matrix[0]

        l = [x for x in matrix[0]]
        c = []
        rx = 1
        ry = -1
        x = len(matrix[0]) - 1
        y = len(matrix) - 1
        xpos = 1
        ypos = x

        top, bottom = 1, y
        left, right = 0, x

        while top <= bottom and left <= right:
            # Move down along the right column (starting from xpos down to bottom)
            for row in range(xpos, bottom + 1):
                l.append(matrix[row][ypos])
            right -= 1
            if top > bottom or left > right:
                break

            # Move left along the bottom row
            for col in range(right, left - 1, -1):
                l.append(matrix[bottom][col])
            bottom -= 1
            if top > bottom or left > right:
                break

            # Move up along the left column
            for row in range(bottom, top - 1, -1):
                l.append(matrix[row][left])
            left += 1
            if top > bottom or left > right:
                break

            # Move right along the top row
            for col in range(left, right + 1):
                l.append(matrix[top][col])
            top += 1

            # Sync your position trackers for the next inner layer
            xpos = top
            ypos = right
            c.append((rx, ry))

        return l