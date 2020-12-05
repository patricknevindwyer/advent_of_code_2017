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
    

if __name__ == "__main__":
    target = int(sys.argv[-1])
    edge_size, largest = grid_square_for(target)
    center_x, center_y = grid_center(edge_size, largest)
    target_x, target_y = grid_location(edge_size, largest, target)
    
    print("target: %d" % (target,))
    print("edge size: %d, largest: %d" % (edge_size, largest))
    print("center (%d, %d)" % (center_x, center_y))
    print("target (%d, %d)" % (target_x, target_y))
    print("distance: %d" % (distance(center_x, center_y, target_x, target_y),))