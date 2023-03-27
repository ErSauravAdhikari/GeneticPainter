import math
import random

import numpy as np


def painter_play(rules, room):
    # returns score, xpos, ypos

    M, N = room.shape

    # Calculates number of squares t to be painted. / #steps allowed
    t = M * N - room.sum()
    t = int(t)

    # add walls
    # env 0 - empty square, 1 - wall/obstruction, 2 - painted square
    env = np.ones((M + 2, N + 2));
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            env[i][j] = 0

    # new room size including walls
    M = M + 2
    N = N + 2

    xpos = [np.nan] * (t + 1)
    ypos = [np.nan] * (t + 1)

    # %random initial location
    while True:
        xpos[0] = math.floor(M * random.random())
        ypos[0] = math.floor(N * random.random())
        if env[xpos[0], ypos[0]] == 0:
            break

    # random itial orientation (up=0,left=-1,right=+1,down=-2)
    direction = math.floor(4 * random.random()) - 2

    # initial score
    score = 0

    for i in range(t):
        # directions -1: Left, 0: Up, 1: Right, 2: Down
        # dx, dy of a forward step (given current direction)
        dx = divmod(direction, 2)[1]
        if direction == -1:
            dx = -1 * dx

        dy = divmod(direction + 1, 2)[1]
        if direction == -2:
            dy = -1 * dy

        # dx, dy of a square to right (given currection direction)
        r_direction = direction + 1
        if r_direction == 2:
            r_direction = -2

        dxr = divmod(r_direction, 2)[1]
        if r_direction == -1:
            dxr = -1 * dxr
        dyr = divmod(r_direction + 1, 2)[1]
        if r_direction == -2:
            dyr = -1 * dyr

        # evaluate surroundings (forward,left,right)
        local = [env[xpos[i] + dx, ypos[i] + dy], env[xpos[i] - dxr, ypos[i] - dyr], env[xpos[i] + dxr, ypos[i] + dyr]]

        # localnum= 2* np.dot([9,3,1], local) if env[xpos[i], ypos[i]] == 2 else 2* np.dot([9,3,1], local) + 1
        localnum = int(2 * np.dot([9, 3, 1], local))
        if env[xpos[i], ypos[i]] == 2:
            localnum += 1

        # use turning rule 1 'turn left', 2 'turn right', 3 'turn left/right 50/50 probabilities'
        if rules[localnum] == 3:
            dirchange = math.floor(random.random() * 2) + 1
        else:
            dirchange = rules[localnum]

        if dirchange == 1:
            direction = direction - 1
            if direction == -3:
                direction = 1
        elif dirchange == 2:
            direction = direction + 1
            if direction == 2:
                direction = -2

        dx = divmod(direction, 2)[1]
        if direction == -1:
            dx = -1 * dx

        dy = divmod(direction + 1, 2)[1]
        if direction == -2:
            dy = -1 * dy

            # paint square
        if env[xpos[i], ypos[i]] == 0:
            env[xpos[i], ypos[i]] = 2
            score = score + 1

        # go forward if possible - stay put if wall/obstacle ahead
        if env[xpos[i] + dx, ypos[i] + dy] == 1:
            xpos[i + 1] = xpos[i]
            ypos[i + 1] = ypos[i]
        else:
            xpos[i + 1] = xpos[i] + dx
            ypos[i + 1] = ypos[i] + dy

            # %normalise score by time
    score = score / t

    return score, xpos, ypos,  # env
