import sys


def grid_square_for(target):
    
    for i in range(2, 1000):
        if (i * i) >= target:
            return i, i * i


def grid_center(edge, largest):
    if largest % 2 == 0:
        # even sqaure, largest is in top left
        x = edge / 2 - 1
        y = edge / 2
        return x, y
    else:
        # odd square, largest is in bottom right
        x = int(edge / 2)
        y = int(edge / 2)
        return x, y


def distance(center_x, center_y, target_x, target_y):
    
    # get the x distance
    
    # get the y distance
    x_dist = max([center_x, target_x]) - min([center_x, target_x])
    y_dist = max([center_y, target_y]) - min([center_y, target_y])

    return x_dist + y_dist
    
    
def grid_location(edge, largest, target):

    x_offset = 0
    y_offset = 0
    
    if largest % 2 == 0:
        # even square, target on top or right
        
        if largest - target < edge:
            # top
            x_offset = (largest - target)
        else:
            # right
            x_offset = edge - 1
            y_offset = (largest - edge + 1) - target
            
    else:
        # odd square, target on left or bottom
        if largest - target < edge:
            # bottom
            x_offset = (largest - target)
            y_offset = edge - 1
        else:
            # left
            y_offset = (largest - edge + 1) - target
    
    return x_offset, y_offset
    

class Grid:
    
    def __init__(self, size=100):
        self._rows = []
        for idx in range(size):
            self._rows.append([0 for i in range(size)])
    
    def neighbor_sum_at(self, x, y):
        nebs = []
        for idx_x_off in [-1, 0, 1]:
            for idx_y_off in [-1, 0, 1]:
                
                # get offsets
                idx_x = x + idx_x_off
                idx_y = y + idx_y_off
                
                # don't count ourself
                if idx_x == x and idx_y == y:
                    continue
                
                # don't go out of bounds
                if idx_x < 0 or idx_x >= len(self._rows):
                    continue
                
                if idx_y < 0 or idx_y >= len(self._rows):
                    continue
                
                nebs.append(self._rows[idx_y][idx_x])
        return sum(nebs)
    
    def set(self, x, y, v):
        self._rows[y][x] = v
    
    def get(self, x, y):
        return self._rows[y][x]


def fill_steps(step_size):
    """
    Generate the steps for the given step size.
    
    Odds go right and then up
    
    Evens go left and then down
    
    """
    steps = []
    
    if step_size % 2 == 0:
        
        for _i in range(step_size):
            steps.append((-1, 0))
        for _i in range(step_size):
            steps.append((0, 1))

    else:
        for _i in range(step_size):
            steps.append((1, 0))
        for _i in range(step_size):
            steps.append((0, -1))
    
    return steps
    
    
if __name__ == "__main__":

    target = int(sys.argv[-1])
    edge_size, largest = grid_square_for(target)
    center_x, center_y = grid_center(edge_size, largest)
    # target_x, target_y = grid_location(edge_size, largest, target)

    print("target: %d" % (target,))
    print("edge size: %d, largest: %d" % (edge_size, largest))
    print("center (%d, %d)" % (center_x, center_y))
    
    # build out our grid
    g = Grid(size=edge_size)
    g.set(center_x, center_y, 1)
    
    # start at the center, start walking edges to do neighbor sums
    loc_x = center_x
    loc_y = center_y
    
    step_size = 1
    steps = fill_steps(step_size)
    
    while g.get(loc_x, loc_y) <= target:
        
        # pop a step, and take it
        step_x, step_y = steps.pop(0)
        loc_x = loc_x + step_x
        loc_y = loc_y + step_y
        
        # fill in our current location
        nsum = g.neighbor_sum_at(loc_x, loc_y)
        g.set(loc_x, loc_y, nsum)
        
        if len(steps) == 0:
            step_size += 1
            steps = fill_steps(step_size)
    print(g.get(loc_x, loc_y))
