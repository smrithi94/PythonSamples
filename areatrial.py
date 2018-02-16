def areaOfASquare(side):
    area=side*side
    return area
def areaOfARectangle(length,breadth):
    area=length*breadth
    return area
def areaOfACircle(radius):
    area=3.14*radius*radius
    return area
side=raw_input('enter the side of the square')
side=float(side)
area1=areaOfASquare(side)
print 'area of the square',area1                
length=raw_input('enter the side of the rectangle')
length=float(length)
breadth=raw_input('enter the breadth of the rectangle')
breadth=float(breadth)
area2=areaOfARectangle(length,breadth)
print 'area of the rectangle',area2
radius=raw_input('enter the radius of the circle')
radius=float(radius)
area3= areaOfACircle(radius)
print 'area of the circle',area3
