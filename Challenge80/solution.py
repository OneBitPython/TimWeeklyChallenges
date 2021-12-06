
def is_point_in_path(x: int, y: int, poly) -> bool:

    num = len(poly)
    j = num - 1
    c = False
    for i in range(num):
        if (x == poly[i][0]) and (y == poly[i][1]):
            # point is a corner
            return True
        if ((poly[i][1] > y) != (poly[j][1] > y)):
            slope = (x-poly[i][0])*(poly[j][1]-poly[i][1]) - (poly[j][0]-poly[i][0])*(y-poly[i][1])
            if slope == 0:
                return True
            if (slope < 0) != (poly[j][1] < poly[i][1]):
                c = not c
        j = i
    return c


for _ in range(int(input())):
    n = int(input())
    string = input()
    string2 = input()
    string = string.split()
    string2 = string2.split()
    sides = []
    sides2 = []
    for i, j in zip(string, string2):
        x, y = map(int, i.split(","))
        x1, y1 = map(int, j.split(","))
        sides.append((x, y))
        sides2.append((x1, y1))

    first_polygon_sides = []
    for i in range(len(sides)-1):
        side = sides[i]+sides[i+1]
        first_polygon_sides.append(side)
    first_polygon_sides.append(sides[-1]+sides[0])

    second_polygon_sides = []
    for i in range(len(sides2)-1):
        side = sides2[i]+sides2[i+1]
        second_polygon_sides.append(side)
    second_polygon_sides.append(sides2[-1]+sides2[0])

    ans = "false"
    br = False
    for side1 in first_polygon_sides:
        if br:
            break
        for side2 in second_polygon_sides:

            a,b,c,d = side1
            w, x, y, z = side2

            dx0 = c-a
            dx1 = y - w
            dy0 = d - b
            dy1 = z - x
            p0 = dy1 * (y-a)-dx1*(z-b)
            p1 = dy1 * (y-c)-dx1*(z-d)
            p2 = dy0 * (c-w)-dx0*(d-x)
            p3 = dy0 * (c-y)-dx0*(d-z)
        
            if (p0*p1 < 0) & (p2*p3 < 0):
                ans = "true"
                br = True
                break
        
    if ans == "true":
        print(ans)
    else:
        for i in sides2:
            if is_point_in_path(i[0], i[1], sides):
                ans = "true"
                break
        if ans == "true":
            print(ans)
        else:
            for side in sides:
                if is_point_in_path(side[0], side[1],sides2):
                    ans = "true"
                    break
            print(ans)
