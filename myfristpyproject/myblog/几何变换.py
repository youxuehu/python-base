from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('C:\\Users\\Public\\Pictures\\Sample Pictures\\Chrysanthemum.jpg')
dst = img.resize((128, 128))
dst = img.rotate(45)  # 顺时针角度表示
dst = img.transpose(Image.FLIP_LEFT_RIGHT)  # 左右互换
dst = img.transpose(Image.FLIP_TOP_BOTTOM)  # 上下互换
dst = img.transpose(Image.ROTATE_90)  # 顺时针旋转
dst = img.transpose(Image.ROTATE_180)
dst = img.transpose(Image.ROTATE_270)
plt.figure("beauty")
plt.subplot(1, 2, 1), plt.title('origin')
plt.imshow(img), plt.axis('off')

box = (80, 100, 260, 300)
roi = img.crop(box)
plt.subplot(1, 2, 2), plt.title('roi')
plt.imshow(roi), plt.axis('off')
plt.show()