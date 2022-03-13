import cv2

facecs = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread(r"C:\Users\Rohit\Desktop\pp\SD.jpg",1)
gray_sc = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = facecs.detectMultiScale(gray_sc,scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)
for x,y,z,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
    
resxed=cv2.resize(img,int(img.shape[1]/2),int(img.shapw[0]/2))
cv2.imshow("RESEZED",resxed)
cv2.waitKey(2000)
cv2.destroyAllWindows()