k = 3
def euclidean(point1, point2):
    """
    Finds the euclidean distance between two points (tuples of k dimensions each)
    """
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)


def closestPoint(allNeighbors, point):
    """
    Brute force way to find the closest point
    """
    minDistance = None
    minPoint = None
    for current in allNeighbors:
        currentDistance = euclidean(point, current)
        if minDistance is None or currentDistance < minDistance:
            minDistance = currentDistance
            minPoint = current
    return minPoint


def build_kdtree(points, depth=0):
    """
    Builds a kdtree
    """
    n = len(points)
    # if no points, can't build a kdtree
    if n <=0:
        return None

    axis = depth % k
    # sort the points based on the axis
    sorted_points = sorted(points, key=lambda point: point[axis])
    # the middle index is the splitting point
    mid = n//2
    # return the point, left subtree and right subtree
    return {
        'point': sorted_points[mid],
        'left': build_kdtree(sorted_points[:mid], depth + 1),
        'right': build_kdtree(sorted_points[mid + 1:], depth + 1)
    }


def kdTreeClosest(root, point, depth=0, nearest=None):
    """
    Finds the nearest neighbor in the kdtree
    """
    if root is None:
        return nearest

    axis = depth % k
    # did we find a better result so far?
    next_best = None
    # the next branch to recurse on
    next_branch = None
    # distance between the searching point and the best result (nearest)
    if nearest is None or euclidean(point, nearest) > euclidean(point, root['point']):
        next_best = root['point']
    else:
        next_best = nearest
    # find which tree to recurse on
    # if item on left, recurse on left
    if point[axis] < root['point'][axis]:
        next_branch = root['left']
    else:
        # recurse right
        next_branch = root['right']

    return kdTreeClosest(next_branch, point, depth+1, next_best)