import cv2

def pencil_sketch(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = cv2.bitwise_not(gray_image)
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    pencil_sketch = cv2.divide(gray_image, blurred_image, scale=256.0)

    cv2.imshow("Original image", image)
    cv2.imshow("Gray image", gray_image)
    cv2.imshow("Inverted image", inverted_image)
    cv2.imshow("Blurred image", blurred_image)
    cv2.imshow("Pencil sketch", pencil_sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows

image_path = "bappa 2 - Copy.jpg"
pencil_sketch(image_path)
