import cv2
import os
images=os.listdir('images')
for i in images:
  image = cv2.imread(f'images/{i}', 1)
  face_cascade = cv2.CascadeClassifier('faces.xml')

  faces = face_cascade.detectMultiScale(image, 1.1, 4)

  for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4)
    try:
      cv2.imwrite(f'face_img/face-{i}', image)
      
    except:
      pass  
