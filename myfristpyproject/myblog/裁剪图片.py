from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('c:/fllow.jpg')  # 打开图像
plt.figure("beauty")
plt.subplot(1, 2, 1), plt.title('origin')
plt.imshow(img), plt.axis('off')

box = (80, 100, 260, 300)
roi = img.crop(box)
plt.subplot(1, 2, 2), plt.title('roi')
plt.imshow(roi), plt.axis('off')
plt.show()
