import cv2, datetime
from time import sleep
from UsbVideoDevice import UsbVideoDevice

'''
rgb_ids = []
ther_ids = []
for id in range(0,10):
    # Windowsの場合にはDirect Showが必要
    # Linuxだと特に必要ない
    # capid=cv2.VideoCapture(id, cv2.CAP_DSHOW)
    capid=cv2.VideoCapture(id)
    if capid.isOpened():
        print(f'id:{id},height:{capid.get(cv2.CAP_PROP_FRAME_HEIGHT)}')
        if capid.get(cv2.CAP_PROP_FRAME_HEIGHT)==120:
            ther_ids.append(id)
        elif capid.get(cv2.CAP_PROP_FRAME_HEIGHT)==360:
            rgb_ids.append(id)
        # ids.append(id)
        # print(f'Video capture{id}:found')
    capid.release()
print(f'rgb_ids{rgb_ids}')
print(f'ther_ids{ther_ids}')
'''

sleep(60)
usbVideoDevice = UsbVideoDevice()
devicelist = usbVideoDevice.getdevicelist()

for (name, cameraId) in devicelist:
    if name=='front_rgb':
        front_rgb_id = cameraId
    elif name=='rear_rgb':
        rear_rgb_id = cameraId
    elif name=='front_ther':
        front_ther_id = cameraId
    elif name=='rear_ther':
        rear_ther_id = cameraId

front_rgb_cam = cv2.VideoCapture(front_rgb_id)
front_ther_cam = cv2.VideoCapture(front_ther_id)
rear_rgb_cam = cv2.VideoCapture(rear_rgb_id)
rear_ther_cam = cv2.VideoCapture(rear_ther_id)

# 1 minitesだけ処理を行う．
looptime = 1
dt_end = datetime.datetime.now() + datetime.timedelta(minutes=looptime)

#繰り返しのためのwhile文
while True:
    #カメラからの画像取得
    front_rgb_ret, front_rgb_frame = front_rgb_cam.read()
    front_ther_ret, front_ther_frame = front_ther_cam.read()
    rear_rgb_ret, rear_rgb_frame = rear_rgb_cam.read()
    rear_ther_ret, rear_ther_frame = rear_ther_cam.read()

    #カメラの画像の出力
    cv2.imshow('front_rgb' , front_rgb_frame)
    cv2.imshow('front_ther' , front_ther_frame)
    cv2.imshow('rear_rgb' , rear_rgb_frame)
    cv2.imshow('rear_ther' , rear_ther_frame)

    #繰り返し分から抜けるためのif文
    key =cv2.waitKey(10)
    if key == 27:
        break

    # 1分後には強制終了させる
    if dt_end < datetime.datetime.now():
        break

#メモリを解放して終了するためのコマンド
front_rgb_cam.release()
front_ther_cam.release()
rear_rgb_cam.release()
rear_ther_cam.release()
cv2.destroyAllWindows()