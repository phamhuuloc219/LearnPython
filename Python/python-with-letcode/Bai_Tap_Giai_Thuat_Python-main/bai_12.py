spiral = 100

import turtle

for circle in range(360):
    big = spiral - 0.4
    spiral = big
    turtle.forward(1)
    turtle.right(big)
    if big <= 0:
        turtle.done
