"""
Image Processing Toolkit - Simple Version
--------------------------------------------
A basic menu-driven program using OpenCV.
No classes, just plain functions and a while loop.

Run:
    pip install opencv-python numpy
    python image_toolkit_simple.py
"""

import cv2

image = None            # the image we are working on
original = None         # a backup of the first loaded image


def load_image():
    global image, original
    path = input("Enter image path: ")
    image = cv2.imread(path)
    if image is None:
        print("Could not load image. Check the path.")
    else:
        original = image.copy()
        print("Image loaded! Size:", image.shape)


def show_image(title):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def to_gray():
    global image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)   # keep 3 channels
    show_image("Grayscale")


def resize():
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


def crop():
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

    if choice == "1":
        x1 = int(input("Top-left x: "))
        y1 = int(input("Top-left y: "))
        x2 = int(input("Bottom-right x: "))
        y2 = int(input("Bottom-right y: "))
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
    elif choice == "2":
        cx = int(input("Center x: "))
        cy = int(input("Center y: "))
        r = int(input("Radius: "))
        cv2.circle(image, (cx, cy), r, color, 2)
    elif choice == "3":
        x1 = int(input("Start x: "))
        y1 = int(input("Start y: "))
        x2 = int(input("End x: "))
        y2 = int(input("End y: "))
        cv2.line(image, (x1, y1), (x2, y2), color, 2)
    else:
        print("Invalid choice")
        return
    show_image("Shape")


def add_text():
    text = input("Enter text: ")
    x = int(input("X position: "))
    y = int(input("Y position: "))
    cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 255), 2)
    show_image("Text Added")


def save_image():
    filename = input("Save as (e.g. output.jpg): ")
    cv2.imwrite(filename, image)
    print("Saved as", filename)


def adjust_brightness_contrast():
    global image
    brightness = int(input("Brightness (-100 to 100): "))
    contrast = float(input("Contrast (1.0 = no change): "))
    image = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    show_image("Brightness/Contrast")


def compare_rgb_bgr():
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imshow("BGR (correct colors)", image)
    cv2.imshow("RGB shown as BGR (colors look swapped)", rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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
    print("10. Brightness/Contrast")
    print("11. Compare RGB vs BGR")
    print("12. Original vs Processed (Side by Side)")
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
        adjust_brightness_contrast()
    elif choice == "11":
        compare_rgb_bgr()
    elif choice == "12":
        side_by_side()
    else:
        print("Invalid choice, try again.")
