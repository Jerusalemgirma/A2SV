def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # layer by layer
        if not matrix or not matrix[0]:
            return []
        height, width = len(matrix), len(matrix[0])
        layer = 0
        direction = 0
        result = []
        while len(result) < height * width:
            if direction == 0:
                result.extend(matrix[layer][layer:width-layer])
            elif direction == 1:
                result.extend((matrix[row][width-layer-1] for row in range(layer + 1, height - layer)))
            elif direction == 2:
                result.extend(matrix[height-layer-1][layer:width-layer-1][::-1])
            else:
                result.extend([matrix[row][layer] for row in range(layer + 1, height - layer - 1)][::-1])
                layer += 1
            direction = (direction + 1) % 4
        return result

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # step by step
        # this solution edits the matrix to mark them as visited
        if not matrix or not matrix[0]:
            return []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current = (0, 0)
        result = []
        current_direction = 0
        while True: # OR: while len(result) < len(matrix) * len(matrix)[0]
            result.append(matrix[current[0]][current[1]])
            matrix[current[0]][current[1]] = '-'
            next_position = self._generate_next(current, current_direction, directions, matrix)
            if next_position:
                current = next_position
            else:
                current_direction = (current_direction + 1) % 4
                next_position = self._generate_next(current, current_direction, directions, matrix)
                if next_position:
                    current = next_position
                else:
                    break
        return result
    
    def _generate_next(self, coord, direction, directions, matrix):
        next_coord = (coord[0] + directions[direction][0], coord[1] + directions[direction][1])
        if 0 <= next_coord[0] < len(matrix) and 0 <= next_coord[1] < len(matrix[0]) and matrix[next_coord[0]][next_coord[1]] != '-':
            return next_coord
        else:
            return None