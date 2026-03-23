import cv2
import numpy as np

def create_cartoon_image(input_path, output_path):
    img = cv2.imread(input_path)
    if img is None:
        print("이미지를 불러올 수 없습니다. 경로를 확인해주세요.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    color = cv2.bilateralFilter(img, 9, 300, 300)

    cartoon = cv2.bitwise_and(color, color, mask=edges)

    cv2.imwrite(output_path, cartoon)
    
    cv2.imshow("Original Image", img)
    cv2.imshow("Cartoon Rendering", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_cartoon_image('test_image.jpg', 'result_image.jpg')