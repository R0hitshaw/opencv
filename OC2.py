import cv2

img = cv2.imread(r"C:\Users\Rohit\Desktop\pp\SD.jpg",1)
rei = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
print(rei.shape)
img_1=cv2.imshow("Resized Image",rei)
cv2.waitKey(0)
cv2.destroyAllWindows()