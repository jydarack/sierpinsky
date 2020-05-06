import numpy as np
import pylab
from random import randint


def midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]


curr_point = [0, 0]  # our seed value for the chaos game
# It can fall anywhere inside the triangle

# our equilateral triangle vertices
v1 = [0, 0]
v2 = [1, 0]
v3 = [0.5, np.sqrt(3) / 2]

# Plot 5000 points
for _ in range(2500):
    # choose a triangle vertex at random
    # set the current point to be the midpoint
    # between the previous current point and
    # the randomly chosen vertex
    val = randint(0, 2)
    if val == 0:
        curr_point = midpoint(curr_point, v1)
    if val == 1:
        curr_point = midpoint(curr_point, v2)
    if val == 2:
        curr_point = midpoint(curr_point, v3)
    # plot the new current point
    pylab.plot(curr_point[0], curr_point[1], "m.", markersize=2)

pylab.show()
