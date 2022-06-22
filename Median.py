import numpy as np

def getD(mask):
  res = np.sum(mask)
  return res if res != 0 else 1

def filter_pixel(n,m,image, length):
  f = np.zeros((length,length))
  for i in range(length):
    for j in range(length):
      f[i][j] = image[n-1+i][m-1+j]
  return np.median(f)


def get_median(image, num):
  res = np.copy(image)
  N, M = res.shape
  for n in range(1, N - num // 2):
    for m in range(1, M - num // 2):
      res[n][m] = filter_pixel(n,m,image, num)
  return res