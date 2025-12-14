import matplotlib.pyplot as plt
import numpy as np

ANGLE = 30
LENGTH_FACTOR = 0.75
INITIAL_LENGTH = 100
COLOR = 'darkred'
LINEWIDTH = 1


def cosd(degrees):
    return np.cos(np.deg2rad(degrees))


def sind(degrees):
    return np.sin(np.deg2rad(degrees))


def draw_tree(x_start, y_start, angle_deg, depth, max_depth, length):
    if depth > max_depth:
        return
    x_end = x_start + length * cosd(angle_deg)
    y_end = y_start + length * sind(angle_deg)
    plt.plot([x_start, x_end], [y_start, y_end], color=COLOR, linewidth=LINEWIDTH)
    draw_tree(x_end, y_end, angle_deg + ANGLE, depth + 1, max_depth, length * LENGTH_FACTOR)
    draw_tree(x_end, y_end, angle_deg - ANGLE, depth + 1, max_depth, length * LENGTH_FACTOR)


def main():
    max_depth = int(input("Please enter the recursion depth (integer between 1 and 12): "))
    plt.figure(figsize=(10, 7))
    plt.axis('off')
    draw_tree(0, 0, 90, 1, max_depth, INITIAL_LENGTH)
    plt.show()


if __name__ == "__main__":
    main()