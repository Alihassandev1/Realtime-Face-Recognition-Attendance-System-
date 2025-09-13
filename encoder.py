import os, re, cv2, face_recognition as fr, pickle
from tqdm import tqdm

images = "images/"
imagesPath = os.listdir(images)
imagesPath = [os.path.join(images, imagePath) for imagePath in imagesPath]

encodedImages = []
encodedId = [re.split(r'[/.]', img)[-2] for img in imagesPath]


def findEncodings(imagesPath):
    print('Encoding Started....')
    for imagePath in tqdm(imagesPath):
        image = cv2.imread(imagePath, cv2.IMREAD_COLOR)
        temp = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # image = fr.load_image_file(temp)
        encoding = fr.face_encodings(temp)
        if encoding:
            encodedImages.append(encoding[0])
    else:
        print('Encoding Completed!')
    return encodedImages

encodedImages = findEncodings(imagesPath)
encodedKnown = [encodedId, encodedImages]

with open('encodedImages.p', 'wb') as f:
    pickle.dump(encodedKnown, f)
    print('File Saved!')