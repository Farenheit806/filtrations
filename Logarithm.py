import numpy as np


def get_logarithmed(image, c):
  image_logarithmed = np.copy(image)
  N, M = image_logarithmed.shape
  for n in range(N):
    for m in range(M):
      image_logarithmed[n][m] = c * np.log(1 + image[n][m])
  return image_logarithmed