import cv2 

img = cv2.imread (r"C:\Users\Rohit\Desktop\pp\SD.jpg", 1)
print(img)
print(type(img))
print(img.shape)
cv2.imshow ("Spiderman",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
