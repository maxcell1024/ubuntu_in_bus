import cv2


#カメラの設定　デバイスIDは0
cap1 = cv2.VideoCapture(3,cv2.CAP_DSHOW)
cap2 = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#繰り返しのためのwhile文
while True:
    #カメラからの画像取得
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if ret1==False:
        print('miss')

    #カメラの画像の出力
    cv2.imshow('camera1' , frame1)
    cv2.imshow('camera2' , frame2)

    #繰り返し分から抜けるためのif文
    key =cv2.waitKey(10)
    if key == 27:
        break

#メモリを解放して終了するためのコマンド
cap1.release()
cap2.release()
cv2.destroyAllWindows()