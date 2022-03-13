import cv2
import time

vd = cv2.VideoCapture(0)

check, frame = vd.read()

print(check)
print(frame)

cv2.imshow("Video",frame)

cv2.waitKey(0)

cv2.destroyAllWindows()


time.sleep(3)

vd.release()