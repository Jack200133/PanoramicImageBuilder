import numpy as np


def translation2D(vector):
    v = vector.copy()

    if (v[2] != 0.):
        v = v / v[2]
    T = np.eye(3)
    T[0:2, 2] = v[0:2]
    return T


def transformvec(H, scorners):
    corners = scorners.copy()
    corners = np.dot(H, corners)
    corners = corners / corners[2, :]
    return corners
