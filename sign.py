import cv2
import numpy as np
import tensorflow as tf

# Load the sign language model
model = tf.keras.models.load_model("sign_language_model.h5")

# Create a video capture object
cap = cv2.VideoCapture(0)

# Get the width and height of the video frame
width = int(cap.get(3))
height = int(cap.get(4))

# Create a black image to draw the signs on
image = np.zeros((height, width, 3), dtype=np.uint8)

# Start a while loop to capture frames from the video
while True:
    # Capture the next frame from the video
    ret, frame = cap.read()

    # If the frame was not captured, break the loop
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the hands in the frame
    hands = cv2.detectMultiScale(gray, 1.1, 4)

    # If no hands were detected, skip the frame
    if len(hands) == 0:
        continue

    # Get the largest hand
    hand = hands[0]

    # Draw the hand on the image
    cv2.rectangle(image, (hand[0], hand[1]), (hand[2], hand[3]), (0, 255, 0), 2)

    # Crop the image to the area of the hand
    crop = image[hand[1]:hand[3], hand[0]:hand[2]]

    # Resize the crop to the size of the model input
    crop = cv2.resize(crop, (224, 224))

    # Convert the crop to a tensor
    crop = tf.convert_to_tensor(crop, dtype=tf.float32)

    # Normalize the tensor
    crop = tf.keras.applications.vgg16.preprocess_input(crop)

    # Make a prediction with the model
    prediction = model.predict(crop)

    # Get the index of the most likely class
    class_index = np.argmax(prediction)

    # Get the name of the class
    class_name = model.classes[class_index]

    # Draw the class name on the image
    cv2.putText(image, class_name, (hand[0], hand[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))

    # Display the image
    cv2.imshow("Sign Language Translator", image)

    # Wait for a key press
    key = cv2.waitKey(1)

    # If the key is Esc, break the loop
    if key == 27:
        break

# Release the video capture object
cap.release()

# Close all open windows
cv2.destroyAllWindows()
