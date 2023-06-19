import cv2

# カメラの読込み
# 内蔵カメラがある場合、下記引数の数字を変更する必要あり
cap = cv2.VideoCapture(0)

# 動画終了まで、1フレームずつ読み込んで表示する。
while(cap.isOpened()):
    # 1フレーム毎　読込み
    ret, frame = cap.read()

    # GUIに表示
    cv2.imshow("Camera", frame)
    # qキーが押されたら途中終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
cv2.destroyAllWindows()
