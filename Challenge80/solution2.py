from shapely.geometry import Polygon
import matplotlib.pyplot as plt
for q in range(int(input())):
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

    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True


    polygon1 = Polygon(sides)
    x, y = polygon1.exterior.xy
    plt.plot(x, y, c="red")


    polygon2 = Polygon(sides2)
    x1, y1 = polygon2.exterior.xy
    plt.plot(x1, y1, c="green")

    plt.show()
