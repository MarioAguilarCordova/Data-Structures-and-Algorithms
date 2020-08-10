# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

import random

N = 5
matrice = [[random.randrange(1, 10) for i in range(N)] for j in range(N)]


def rotate_matrix(matrix, degrees):
    rotated_matrix = [[random.randrange(1, 10) for i in range(N)] for j in range(N)]


rotate_matrix(matrice, 90)

print(matrice)

for i in range(5):
    print(matrice[i])
