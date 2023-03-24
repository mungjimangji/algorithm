def solution(dots):
    def slope(points):
        x1, y1 = points[0]
        x2, y2 = points[1]
        return (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')

    def isParallel(line1, line2):
        return slope(line1) == slope(line2)

    first_dot = dots[0]
    for dot in dots[1:]:
        line1 = [first_dot, dot]
        line2 = [d for d in dots if d not in line1]
        if isParallel(line1, line2):
            return 1
    return 0