from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('c:/fllow.jpg')
gray = img.convert('L')
plt.figure("beauty")
plt.imshow(gray, cmap='gray')
plt.axis('off')
plt.show()
