import numpy as np


def get_negative(image):
  image_negative = np.copy(image)
  N, M = image_negative.shape
  for n in range(N):
    for m in range(M):
      image_negative[n][m] = 254 - 1 - image[n][m]
  return image_negative