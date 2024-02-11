from Classes import Point, Line

def find_parallel_lines(points, lines):
    if len(points) < 2 or len(lines) == 0:
        return 1
    best = [points[0], points[1], 0]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            now = [points[i], points[j], 0]
            now_line = Line(now[0].x, now[0].y, now[1].x, now[1].y)
            for l in lines:
                if now_line.parallel(l):
                    now[2] += 1
            if best[2] < now[2]:
                best = now
    if best[2] == 0:
        return 2
    return best
