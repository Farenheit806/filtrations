import numpy as np

def getD(mask):
  res = np.sum(mask)
  return res if res != 0 else 1

def filter_pixel(n,m,image,mask, D, B, length):
  sum_ = 0
  for i in range(length):
    for j in range(length):
      sum_ += image[i-length//2+n][j - length//2 + m]*mask[i - length//2][j - length//2]
  return sum_ * 1 / D + B

def get_Sobel(image, is_X = True):
  image_avged = np.copy(image)
  N, M = image_avged.shape
  mask = masks(is_X)
  num, numY = mask.shape
  D = getD(mask)
  for n in range(1, N - num // 2):
    for m in range(1, M - num // 2):
      image_avged[n][m] = filter_pixel(n,m,image,mask, D, 0, num)
  return image_avged

def masks(is_X):
  if is_X:
    return np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
  else:
    return np.array([[-1,0,1],[-2,0,2],[-1,0,1]])