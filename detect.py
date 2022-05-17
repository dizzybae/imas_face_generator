import cv2
import sys
import os
import os.path
import shutil


def detect(filename,cascade_file="lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     #scaleFactor>1,越大选取越接近正脸
                                     #minsize：每次检测框选的范围。越大得到的脸越少
                                     
                                     minNeighbors=4,
                                     minSize=(50, 50))

  #  for (x, y, w, h) in faces:
  #

    count=0
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            # 在图上画矩形框
            #cv2.rectangle(image, (x, y), (x + w, y + h), (255,255,255), 2)
            cv2.imwrite('./cropped/{}_{}.jpg'.format(filename, count),
                        image[y:y+h, x: x + w])
         #   cv2.imwrite('./img/image_{}.png'.format(count), image[int(y - 0.1 * h): int(y + 0.9 * h), x: x + w])
            count+=1

    else:
        return False;
    #cv2.imshow("faceresults", image)
    cv2.waitKey(0)
    return True;


#显示检测人脸结果
#    cv2.imshow("faceresults", faces)
 #   cv2.waitKey(0)
  #  cv2.imwrite("out.png", image)


if len(sys.argv) != 2:
    sys.stderr.write("usage: detect.py <filename> \n")
    sys.exit(-1)

img_dir = sys.argv[1]
files = os.listdir(img_dir)
ct=0
for f in files:
    if detect(os.path.join(img_dir, f)):
        ct += 1
        print(ct)
