import datetime
from UsbVideoDevice import UsbVideoDevice
from time import sleep
import cv2
import os

# カメラのIDを取得する
# devicelist → [('front_ther', 4), ('front_rgb', 6), ('rear_rgb', 0), ('rear_ther', 2)]
def get_cam_id(camera_name :str)-> int:
    usbVideoDevice = UsbVideoDevice()
    devicelist = usbVideoDevice.getdevicelist() 
    for (name, cameraId) in devicelist:
        if name==camera_name:
            return cameraId
        elif name==camera_name:
            return cameraId
        elif name==camera_name:
            return cameraId
        elif name==camera_name:
            return cameraId
   
def assert_isopened(cam :cv2.VideoCapture):
    assert cam.isOpened()

# データを保存するディレクトリを作成する
def makedir(dirname :str)->str:
    dir_name=datetime.datetime.now().strftime('%Y%m%d')

    # 撮影日のディレクトリを作成
    if dirname=='common':
        common_output_dir = "/home/inet-lab/minato_camera_in_bus/mp4/" + dir_name
        if(not (os.path.exists(common_output_dir))):
            os.mkdir(common_output_dir)
        return common_output_dir

    # 撮影日のディレクトリの下にfrontカメラのディレクトリを作成
    if dirname=='front':
        front_output_dir = "/home/inet-lab/minato_camera_in_bus/mp4/" + dir_name + "/front/"
        if(not (os.path.exists(front_output_dir))):
            os.mkdir(front_output_dir)
        return front_output_dir

    # 撮影日のディレクトリの下にrearカメラのディレクトリを作成
    if dirname=='rear':
        rear_output_dir = "/home/inet-lab/minato_camera_in_bus/mp4/" + dir_name + "/rear/"
        if(not (os.path.exists(rear_output_dir))):
            os.mkdir(rear_output_dir)
        return rear_output_dir

def ret_check(cam :cv2.VideoCapture):
    ret, frame = cam.read()
    assert ret, 'frameがNoneになっています．もう一度プログラムを起動してください．'


def file_name(cam :str):
    strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M')
    if str(cam) in 'front_rgb':
        _file = 'front_rgb_video'
        _output_dir=makedir('front')

    elif str(cam) in 'front_ther':
        _file = 'front_ther_video'
        _output_dir=makedir('front')

    elif str(cam) in 'rear_rgb':
        _file = 'rear_rgb_video'
        _output_dir=makedir('rear')
    elif str(cam) in 'rear_ther':
        _file = 'rear_ther_video'
        _output_dir=makedir('rear')

    filename = _output_dir + _file + strdate + '.mp4'
    return filename




if __name__ == '__main__':
    # カメラのID決定
    sleep(5)
    front_rgb_cam = cv2.VideoCapture(get_cam_id('front_rgb'))
    front_ther_cam = cv2.VideoCapture(get_cam_id('front_ther'))
    rear_rgb_cam = cv2.VideoCapture(get_cam_id('rear_rgb'))
    rear_ther_cam = cv2.VideoCapture(get_cam_id('rear_ther'))

    # カメラのオブジェクトを取得できているかのチェック
    assert_isopened(front_rgb_cam)
    assert_isopened(front_ther_cam)
    assert_isopened(rear_rgb_cam)
    assert_isopened(rear_ther_cam)

    # frameをキャプチャできているかのチェック
    ret_check(front_rgb_cam)
    ret_check(front_ther_cam)
    ret_check(rear_rgb_cam)
    ret_check(rear_ther_cam)

    # ファイルを保存するディレクトリの作成
    common_output_dir=makedir('common')
    front_output_dir=makedir('front')
    rear_output_dir=makedir('rear')

    # 動画ファイル保存用の設定
    fps = 9

    rgb_w = int(front_rgb_cam.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    ther_w = int(front_ther_cam.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    rgb_h = int(front_rgb_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    ther_h = int(front_ther_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')        # 動画保存時のfourcc設定（mp4用）
    strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M')
    front_rgb_filename = front_output_dir + "front_rgb_video" + strdate + ".mp4"
    front_ther_filename = front_output_dir + "front_ther_video" + strdate + ".mp4"
    front_rgb_video = cv2.VideoWriter(front_rgb_filename, fourcc, fps, (rgb_w, rgb_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
    front_ther_video = cv2.VideoWriter(front_ther_filename, fourcc, fps, (ther_w, ther_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）

    rear_rgb_filename = rear_output_dir + "rear_rgb_video" + strdate + ".mp4"
    rear_ther_filename = rear_output_dir + "rear_ther_video" + strdate + ".mp4"
    rear_rgb_video = cv2.VideoWriter(rear_rgb_filename, fourcc, fps, (rgb_w, rgb_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
    rear_ther_video = cv2.VideoWriter(rear_ther_filename, fourcc, fps, (ther_w, ther_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）

    # 10 minitesだけ処理を行う．
    looptime = 10
    dt_end = datetime.datetime.now() + datetime.timedelta(minutes=looptime)

    # 撮影＝ループ中にフレームを1枚ずつ取得（qキーで撮影終了）
    while(True):
        front_rgb_ret, front_rgb_frame = front_rgb_cam.read()
        front_ther_ret, front_ther_frame = front_ther_cam.read()
        rear_rgb_ret, rear_rgb_frame = rear_rgb_cam.read()
        rear_ther_ret, rear_ther_frame = rear_ther_cam.read()

        front_rgb_video.write(front_rgb_frame)                                     # 動画を1フレームずつ保存する
        front_ther_video.write(front_ther_frame)                                     # 動画を1フレームずつ保存する
        rear_rgb_video.write(rear_rgb_frame)                                     # 動画を1フレームずつ保存する
        rear_ther_video.write(rear_ther_frame)                                     # 動画を1フレームずつ保存する

        # キー操作があればwhileループを抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        sleep(1/fps)
        if dt_end < datetime.datetime.now():
            # ファイルを保存するディレクトリの作成
            common_output_dir=makedir('common')
            front_output_dir=makedir('front')
            rear_output_dir=makedir('rear')

            dt_end = dt_end + datetime.timedelta(minutes=looptime)
            strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M')
            # ファイルの保存
            front_rgb_filename = front_output_dir + "front_rgb_video" + strdate + ".mp4"
            front_ther_filename = front_output_dir + "front_ther_video" + strdate + ".mp4"
            front_rgb_video = cv2.VideoWriter(front_rgb_filename, fourcc, fps, (rgb_w, rgb_h)) 
            front_ther_video = cv2.VideoWriter(front_ther_filename, fourcc, fps, (ther_w, ther_h))

            rear_rgb_filename = rear_output_dir + "rear_rgb_video" + strdate + ".mp4"
            rear_ther_filename = rear_output_dir + "rear_ther_video" + strdate + ".mp4"
            rear_rgb_video = cv2.VideoWriter(rear_rgb_filename, fourcc, fps, (rgb_w, rgb_h)) 
            rear_ther_video = cv2.VideoWriter(rear_ther_filename, fourcc, fps, (ther_w, ther_h))
  
            print(f'create new file {dt_end}')


    # 撮影用オブジェクトとウィンドウの解放
    front_rgb_cam.release()
    front_ther_cam.release()
    rear_rgb_cam.release()
    rear_ther_cam.release()
    cv2.destroyAllWindows()
