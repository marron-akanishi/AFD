import sys
import cv2
import dlib

# 顔検出器
face_detector = dlib.simple_object_detector("./detector_face.svm")
# 目検出器
eye_detector = dlib.simple_object_detector("./detector_eye.svm")

def detect(img_path):
    # 画像ファイルを開く
    image = cv2.imread(img_path)
    # 顔の検出
    faces = face_detector(image)
    if len(faces) > 0:
        for rect in faces:
            # 座標取得
            x_start = rect.left()
            x_end = rect.right()
            y_start = rect.top()
            y_end = rect.bottom()
            # サイズ取得
            face_width = x_end - x_start
            face_height = y_end - y_start
            # 長方形の場合、弾く
            if abs(face_width - face_height) > 3:
                continue
            # 顔部分を切り抜き
            face = image[y_start:y_end, x_start:x_end]
            # 目の検出
            eyes = eye_detector(face)
            if len(eyes) > 0:
                for eye in eyes:
                    cv2.rectangle(image, (x_start+eye.left(), y_start+eye.top()),
                                  (x_start+eye.right(), y_start+eye.bottom()), (255, 0, 0), thickness=2)
            else:
                continue
            # 顔部分を赤線で囲う
            # OpenCVの画像は色指定がBGRとなる
            cv2.rectangle(image, (x_start, y_start), (x_end, y_end), (0, 0, 255), thickness=2)
    # 顔部分を赤線で囲った画像の保存
    cv2.imwrite(img_path, image)

if __name__ == '__main__':
    detect(sys.argv[1])
