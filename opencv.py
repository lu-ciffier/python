import cv2

img_name = r"C:\Users\Lucifer\Desktop\shebao.png"
img = cv2.imread(img_name)
cv2.imshow("figure", img)
print(img.shape)