import math
import sys


def quadratic_formula(a, b, c):
    """ Return the solutions to the equation ax^2 + bx + c = 0. """
    # Compute the descriminant
    disc = b**2 - 4 * a * c
    # Compute the two roots
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b + math.sqrt(disc)) / (2 * a)
    return (root1, root2)


if __name__ == '__main__':
    try:
        roots = quadratic_formula(
            int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        print(roots)
    except Exception as e:
        print("first argument a cannot be a 0")
