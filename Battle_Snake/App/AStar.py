def printg(grid, name):
    print '%s: [' % name
    for row in grid:
        print row
    print ']'

def dist(p, q):
    dx = abs(p[0] - q[0])
    dy = abs(p[1] - q[1])
    return dx + dy;

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current =  came_from[current]
        total_path.append(current)
    return list(reversed(total_path))

def neighbours(node, grid, score, tail, ignore_list):
    width = len(grid)
    height = len(grid[0])

    subtail = []
    if score >= len(tail):
        subtail = [tuple(x) for x in tail]
    else:
        subtail = [tuple(x) for x in tail[len(tail)-score:]]

    result = []
    if (node[0] > 0):
        result.append((node[0]-1,node[1]))
    if (node[0] < width-1):
        result.append((node[0]+1,node[1]))
    if (node[1] > 0):
        result.append((node[0],node[1]-1))
    if (node[1] < height-1):
        result.append((node[0],node[1]+1))

    result = filter(lambda p: (grid[p[0]][p[1]] not in ignore_list) or (p in subtail), result)

    return result

def a_star(start, goal, grid, tail):
    start = tuple(start)
    goal = tuple(goal)

    closed_set = []
    open_set   = [start]
    came_from = {} #empty map

    g_score = [[10000 for x in xrange(len(grid[y]))] for y in xrange(len(grid))]
    g_score[start[0]][start[1]] = 0

    f_score = [[10000 for x in xrange(len(grid[y]))] for y in xrange(len(grid))]
    f_score[start[0]][start[1]] = dist(start,goal)

    while(len(open_set) > 0):
        current = min(open_set, key=lambda p: f_score[p[0]][p[1]])

        if (current == goal):
            return reconstruct_path(came_from, goal)

        open_set.remove(current)
        closed_set.append(current)

        for neighbour in neighbours(current, grid, g_score[current[0]][current[1]], tail,[1,2,5]):
            if neighbour in closed_set:
                continue
            tentative_g_score = g_score[current[0]][current[1]] + dist(current,neighbour)
            if neighbour not in open_set:
                open_set.append(neighbour)
            elif tentative_g_score >= g_score[neighbour[0]][neighbour[1]]:
                continue

            came_from[neighbour] = current
            g_score[neighbour[0]][neighbour[1]] = tentative_g_score
            f_score[neighbour[0]][neighbour[1]] = tentative_g_score + dist(neighbour,goal)

    return None

#print a_star((3,1),(0,1),[[0,2,0,0],[0,2,0,0],[1,2,0,0],[0,2,0,0]], [[3,1],[2,1],[1,1],[0,1]])
#print a_star((0,4),(3,4),[[0,2,0,0,2,0],[0,2,0,1,2,2],[0,2,2,2,2,2],[0,0,1,0,0,0]],[[0,4],[1,4],[1,5],[2,5],[2,4],[2,3],[2,2],[2,1],[1,1],[1,0]])
