"""
Image Processing Toolkit 

Run:
    pip install opencv-python numpy
    python image_toolkit_simple.py
"""

import cv2 # Imports OpenCV, the library used for all image loading, editing, and display operations.

image = None            # the image we are working on
original = None         # a backup of the first loaded image


def load_image():
    global image, original #tells Python this function will 
    # reassign the module-level image and original variables, not create new local ones.
    path = input("Enter image path: ")
    image = cv2.imread(path)
    if image is None:
        print("Could not load image. Check the path.")
    else:
        original = image.copy() #without .copy(), original would just point to the same image, so future edits would change both
        print("Image loaded! Size:", image.shape)


def show_image(title):
    cv2.imshow(title, image) #Opens a window with the given title showing the current image
    cv2.waitKey(0) #cv2.waitKey(0) pauses execution indefinitely until a key is pressed
    cv2.destroyAllWindows() #destroyAllWindows() then closes the window. 
    #This is called after almost every edit so you can see the result.


def to_gray():
    global image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   #keep 1 channel
    image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)   # keep 3 channels
    show_image("Grayscale")


def resize(): #Asks for new width/height as integers, then resizes the image
    global image
    w = int(input("New width: "))
    h = int(input("New height: "))
    image = cv2.resize(image, (w, h))
    show_image("Resized")


def rotate():
    global image
    print("1. 90 degrees  2. 180 degrees  3. 270 degrees")
    choice = input("Choose: ")
    if choice == "1":
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif choice == "2":
        image = cv2.rotate(image, cv2.ROTATE_180)
    elif choice == "3":
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    else:
        print("Invalid choice")
        return
    show_image("Rotated")


def flip():
    global image
    print("1. Horizontal  2. Vertical  3. Both")
    choice = input("Choose: ")
    if choice == "1":
        image = cv2.flip(image, 1)
    elif choice == "2":
        image = cv2.flip(image, 0)
    elif choice == "3":
        image = cv2.flip(image, -1)
    else:
        print("Invalid choice")
        return
    show_image("Flipped")


def crop(): #Takes two corner coordinates and crops using NumPy array slicing
    global image
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    image = image[y1:y2, x1:x2]
    show_image("Cropped")


def draw_shape():
    print("1. Rectangle  2. Circle  3. Line")
    choice = input("Choose: ")
    color = (0, 255, 0)   # green, simple fixed color
#draw_shape doesn't declare global image because it's only mutating the image in place 
# via cv2.rectangle/cv2.circle/cv2.line, not reassigning the image variable itself

    if choice == "1": #draws a rectangle using coordinates
        x1 = int(input("Top-left x: "))
        y1 = int(input("Top-left y: "))
        x2 = int(input("Bottom-right x: "))
        y2 = int(input("Bottom-right y: "))
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
    elif choice == "2": #draws a circle using center and radius
        cx = int(input("Center x: "))
        cy = int(input("Center y: "))
        r = int(input("Radius: "))
        cv2.circle(image, (cx, cy), r, color, 2)
    elif choice == "3": #draws a line using two endpoints
        x1 = int(input("Start x: "))
        y1 = int(input("Start y: "))
        x2 = int(input("End x: "))
        y2 = int(input("End y: "))
        cv2.line(image, (x1, y1), (x2, y2), color, 2)
    else:
        print("Invalid choice")
        return
    show_image("Shape")


def add_text(): #adds text over image
    text = input("Enter text: ")
    x = int(input("X position: "))
    y = int(input("Y position: "))
    cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 255), 2) #white color text 
    show_image("Text Added")


def save_image():
    filename = input("Save as (e.g. output.jpg): ")
    cv2.imwrite(filename, image)
    print("Saved as", filename)


def side_by_side():
    import numpy as np
    h = 300
    img1 = cv2.resize(original, (int(original.shape[1]*h/original.shape[0]), h))
    img2 = cv2.resize(image, (int(image.shape[1]*h/image.shape[0]), h))
    combined = np.hstack((img1, img2))
    cv2.imshow("Original vs Processed", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def menu():
    print("\n----- IMAGE PROCESSING TOOLKIT -----")
    print("1. Load Image")
    print("2. Grayscale")
    print("3. Resize")
    print("4. Rotate")
    print("5. Flip")
    print("6. Crop")
    print("7. Draw Shape")
    print("8. Add Text")
    print("9. Save Image")
    print("10. Original vs Processed (Side by Side)")
    print("0. Exit")


while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "0":
        print("Bye!")
        break
    elif choice == "1":
        load_image()
    elif image is None:
        print("Please load an image first (Option 1).")
    elif choice == "2":
        to_gray()
    elif choice == "3":
        resize()
    elif choice == "4":
        rotate()
    elif choice == "5":
        flip()
    elif choice == "6":
        crop()
    elif choice == "7":
        draw_shape()
    elif choice == "8":
        add_text()
    elif choice == "9":
        save_image()
    elif choice == "10":
        side_by_side()
    else:
        print("Invalid choice, try again.")
