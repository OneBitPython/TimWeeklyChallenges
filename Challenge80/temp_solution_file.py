def solution():
    class P:
        def __init__(self,x,y):self.x=x;self.y=y
    def ccw(A,B,C):return (C.y-A.y)*(B.x-A.x)>(B.y-A.y)*(C.x-A.x)
    
    def intersect(A,B,C,D):return ccw(A,C,D)!=ccw(B,C,D)and ccw(A,B,C)!=ccw(A,B,D)
    
    def is_point_in_path(x: int, y: int, poly) -> bool:
    
        num = len(poly)
        j = num - 1
        c = False
        for i in range(num):
            if (x == poly[i].x) and (y == poly[i].y):
                # point is a corner
                return True
            if ((poly[i].y > y) != (poly[j].y > y)):
                slope = (x-poly[i].x)*(poly[j].y-poly[i].y) - (poly[j].x-poly[i].x)*(y-poly[i].y)
                if slope == 0:
                    return True
                if (slope < 0) != (poly[j].y < poly[i].y):
                    c = not c
            j = i
        return c
    
    
    
    for m in[p:=input]*int(p()):
        sides=int(p());intsct=False
        polygon1=[P(int(char.split(',')[0]),int(char.split(',')[1]))for char in p().split()]
        polygon2=[P(int(char.split(',')[0]),int(char.split(',')[1]))for char in p().split()]
        for i, point in enumerate(polygon1):
            if intsct:break
            for o,_point in enumerate(polygon2):
                if intsct:break
                if i==sides-1:next_point=polygon1[0]
                else:next_point=polygon1[i+1]
                if o==sides-1:nextpoint_=polygon2[0]
                else:nextpoint_=polygon2[o+1]
                if intersect(point,next_point,_point,nextpoint_) or point==_point:intsct = True
        if not intsct:
            for side in polygon1:
                x,y=side.x, side.y
                if is_point_in_path(x,y,polygon2):
                    intsct=True
                    break
            if not intsct:
                for side in polygon2:
                    x,y=side.x, side.y
                    if is_point_in_path(x,y,polygon1):
                        intsct=True
                        break
        print(str(intsct).lower())
