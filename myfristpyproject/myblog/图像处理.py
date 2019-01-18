from PIL import Image

# img = Image.open('C:\\Users\\Public\\Pictures\\Sample Pictures\\Chrysanthemum.jpg')
# img.show()

import matplotlib.pyplot as plt

img = Image.open('C:\\Users\\Public\\Pictures\\Sample Pictures\\Chrysanthemum.jpg')
plt.figure('dog')
plt.imshow(img)
plt.axis('off')
print(img.size)
print(img.mode)
print(img.format)
plt.show()
img.save('c:\\fllow.jpg')



