import cv2
for id in range(0,10):
    capid=cv2.VideoCapture(id, cv2.CAP_DSHOW)
    if capid.isOpened():
        print(capid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if capid.get(cv2.CAP_PROP_FRAME_HEIGHT)==122:
            print(f'therid:{capid.get(cv2.CAP_PROP_FRAME_HEIGHT)}')
            print(f'therid:{id}')
            ther_cid=id
        elif capid.get(cv2.CAP_PROP_FRAME_HEIGHT)==360:
            print(f'rgbid:{capid.get(cv2.CAP_PROP_FRAME_HEIGHT)}')
            rgb_cid=id
            print(f'rgbid:{id}')
        # ids.append(id)
        # print(f'Video capture{id}:found')
    else:
        print(f'Video capture{id}:None')
    capid.release()

print(f'therid:{ther_cid}')
print(f'rgbid:{rgb_cid}')
#カメラの設定　デバイスIDは0
# cap1 = cv2.VideoCapture(ther_cid-1)
cap1 = cv2.VideoCapture(rgb_cid,cv2.CAP_DSHOW)

#繰り返しのためのwhile文
while True:
    #カメラからの画像取得
    ret1, frame1 = cap1.read()
    # ret2, frame2 = cap2.read()

    if ret1==False:
        print('miss')

    #カメラの画像の出力
    cv2.imshow('camera1' , frame1)
    # cv2.imshow('camera2' , frame2)

    #繰り返し分から抜けるためのif文
    key =cv2.waitKey(10)
    if key == 27:
        break

#メモリを解放して終了するためのコマンド
cap1.release()
# cap2.release()
cv2.destroyAllWindows()