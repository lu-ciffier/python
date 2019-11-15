import matplotlib.pyplot as plt
from matplotlib.image import imread

img_name = r"C:\Users\Lucifer\Desktop\shebao.png"
img = imread(img_name)
plt.imshow(img)
plt.show()