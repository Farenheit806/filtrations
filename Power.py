import numpy as np


def get_powered(image, c, g, eps = 0):
  image_powered = np.copy(image)
  N,M = image_powered.shape
  for n in range(N):
    for m in range(M):
      image_powered[n][m] = c * np.power((image[n][m] + eps), g)
  return image_powered