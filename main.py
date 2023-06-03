import cv2 as cv

# Load face cascade for face recognition
face_cascade = cv.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
# Load eye cascade for eye recognition
eye_cascade = cv.CascadeClassifier('classifiers/haarcascade_eye.xml')

# Define font and colors
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 0.5
fontColor = (255, 255, 255)
fontThickness = 2
rectFaceColor = (255, 0, 0)
rectFaceBorderWidth = 2
rectEyeColor = (0, 255, 0)
rectEyeBorderWidth = 2

# Open camera
cap = cv.VideoCapture(0)

while True:
    # Read camera frame
    ret, frame = cap.read()

    # Mirror frame
    frame = cv.flip(frame, 1)

    # Detect faces
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    # Detect eyes
    eyes = eye_cascade.detectMultiScale(frame, 1.3, 10)

    # Draw rectangle around faces
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), rectFaceColor, rectFaceBorderWidth)
        # Place label
        label = 'Face'
        cv.putText(frame, label, (x, y-10), font, fontScale, fontColor, fontThickness)

    # Draw rectangle around right eyes
    for (x, y, w, h) in eyes:
        cv.rectangle(frame, (x, y), (x+w, y+h), rectEyeColor, rectEyeBorderWidth)
        # Place label
        label = 'Eye'
        cv.putText(frame, label, (x, y-10), font, fontScale, fontColor, fontThickness)

    # Show frame
    cv.imshow('Video', frame)
    
    # Wait for 'x' key to exit
    if cv.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()             # Release camera
cv.destroyAllWindows()    # Close windows