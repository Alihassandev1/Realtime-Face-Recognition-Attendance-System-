import cv2, face_recognition as fr, pickle
from datetime import datetime, time, date
from time import sleep
import json, tqdm


with open('out.json', 'r') as f:
    data = json.load(f)

print('Loading Encoded Files...')
with open('encodedImages.p', 'rb') as f:
    encodedKnown = pickle.load(f)
encodedId, encodedImages = encodedKnown
print('Loading Complete.')
count = 0

source = cv2.VideoCapture(0)
print('processing...')
while cv2.waitKey(1) != 27:
    ret, img = source.read()
    if not ret:
        break
    img = cv2.flip(img, 1)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    # print(imgS.shape)
    facesCurFrame = fr.face_locations(imgS)
    encodesCurFrame = fr.face_encodings(imgS, facesCurFrame)
    if facesCurFrame:
        for encodeFace, faceLoc in tqdm.tqdm(zip(encodesCurFrame, facesCurFrame)):
            matches = fr.compare_faces(encodedImages, encodeFace)
            faceDis = fr.face_distance(encodedImages, encodeFace)
            # print('Matches: ',matches)
            # print('Face Distance: ',faceDis)
            matchIndex = faceDis.argmin()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            if matches[matchIndex]:
                id = encodedId[matchIndex]
                name = data[id]['name']

                currTm = datetime.now()
                lastAttendTime = datetime.strptime(data[id]['last Attendence Time'], "%Y-%m-%d %H:%M:%S")

                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

                start = time(22, 50)
                end = time(23, 11)

                if start <= datetime.now().time() <= end:
                    data[id]['total Attendence'] += 1
                    data[id]['last Attendence Time'] = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    msg = f'Welcome {name} Your Attendence is Marked!'
                    cv2.putText(img, msg, (10, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
                    sleep(2)
                    break

                lastAttend = data[id]['last Attendence Time'].split(' ')[0]
                today = str(date.today())
                
                if lastAttend == today: 
                    msg = f'Your Attendence is already Marked today {name}! at {data[id]["last Attendence Time"].split(' ')[1]}'
                    cv2.putText(img, msg, (10, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
                    
                else:
                    msg = f'{name} Ensure presence between {start} to {end}!!!'
                    cv2.putText(img, msg, (10, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
            else:
                cv2.putText(img, 'Anonymous', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
    else:
        msg = "No Face Found"
        cv2.putText(img, msg, (10, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

    cv2.imshow('Webcam', img)

source.release()
cv2.destroyAllWindows()

print('Updating Student Data....')
with (open('out.json', 'w')) as f:
    json.dump(data, f, indent=4)
print('Update Data Sucessfully!\nfile Saved!')
