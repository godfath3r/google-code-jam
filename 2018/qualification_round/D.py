from math import sqrt, acos, cos, sin, degrees


x = degrees(acos( 1.414213 / sqrt(2)))
print x

matrix = [[1,      0,       0],
          [0, cos(x), -sin(x)],
          [0, sin(x), cos(x)]]

a = [0, 0, 0.5]
b = [0, 0.5, 0]
c = [0.5, 0, 0]
print "cos", cos(x)
print "sin", sin(x)