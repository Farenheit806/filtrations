from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

from Negative import get_negative
from Power import get_powered
from Sobel import get_Sobel
from Avg import get_avg
from Logarithm import get_logarithmed
from Median import get_median

if __name__ == '__main__':
  image = np.array(Image.open("1.jpg").convert("L"))
  image_negative = get_negative(image)
  image_powered = get_powered(image, 0.5, 0.5)
  image_logged = get_logarithmed(image, 0.5)
  image_avged = get_avg(image, 3)
  image_Sobel_X = get_Sobel(image)
  image_Sobel_Y = get_Sobel(image, False)
  image_median = get_median(image,3)

  fig, axs = plt.subplots(3,3)

  axs[0,0].imshow(image, cmap="gray")
  axs[0,1].imshow(image_negative, cmap="gray")
  axs[0,2].imshow(image_powered, cmap="gray")
  axs[1,0].imshow(image_logged, cmap="gray")
  axs[1,1].imshow(image_avged, cmap="gray")
  axs[1,1].imshow(image_avged, cmap="gray")
  axs[1,2].imshow(image_Sobel_X, cmap="gray")
  axs[2,0].imshow(image_Sobel_Y, cmap="gray")
  axs[2,1].imshow(image_median, cmap="gray")

  axs[0,0].set(title="Оригинальное изображение")
  axs[0,1].set(title="Негатив")
  axs[0,2].set(title="Степенное преобразование")
  axs[1,0].set(title="Логарифмическое преобразование")
  axs[1,1].set(title="Скользящее среднее")
  axs[1,2].set(title="Оператор Собеля X")
  axs[2,0].set(title="Оператор Собеля Y")
  axs[2,1].set(title="Медианальное")

  plt.show()