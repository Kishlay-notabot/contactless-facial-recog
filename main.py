import cv2
from datetime import *
from cv2 import FONT_HERSHEY_DUPLEX
from simple_facerec import SimpleFacerec
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")
cap = cv2.VideoCapture(0)
def markAttendance(name):
    print(name)
    with open('Attendance.csv','r+') as f:
        mydatalist = f.readlines()
        print(mydatalist)
        namelist = []        
        for line in mydatalist:
            entry = line.split(',')
            namelist.append(entry[0])
            # print(namelist)
            # print(entry[0])
            if (name not in namelist):
                now = datetime.now()
                dtstring = now.strftime('%H:%M:%S')
                f.writelines(f'{name},{dtstring}')
                print(name)


def rec_face():
    while True:
        ret, frame = cap.read()
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x1, y2, x2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            cv2.putText(frame, name, (x1, y1 -10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0),2)
            cv2.rectangle(frame, (x1,y1), (x2, y2), (0, 0, 200), 2)
        cv2.imshow("Frame", frame)
        markAttendance(face_names)

        key = cv2.waitKey(1)
        if key == 27:
            break



rec_face()
cap.release()
cv2.destroyAllWindows()
