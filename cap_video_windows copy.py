import datetime
from time import sleep
import cv2
import os

# カメラのIDがrgbかtherかをframeの差分を見て判斷
# def is_ther(frame) -> bool:
#     """frame from thermo capture"""
#     vs01 = np.all(frame[:, :, 0] == frame[:, :, 1])
#     vs12 = np.all(frame[:, :, 1] == frame[:, :, 2])
#     vs20 = np.all(frame[:, :, 2] == frame[:, :, 0])
#     return vs01 and vs12 and vs20

# カメラのIDを取得
# def get_camera_ids() -> tuple[int, int]:
#     rgb_cid, ther_cid = None, None
#     for i in range(10):
#         print(i)
#         tmp_capture = cv2.VideoCapture(i, cv2.CAP_DSHOW)
#         ret, frame = tmp_capture.read()
#         if frame is not None:
#             if is_ther(frame):
#                 ther_cid = i
#                 print("Define thermal ID")
#             else:
#                 rgb_cid = i
#                 print("Define rgb ID")
#         tmp_capture.release()
#     assert rgb_cid is not None and ther_cid is not None, 'ERROR: Camera ids is not found'
#     return rgb_cid, ther_cid

if __name__ == '__main__':
    # カメラのID決定
    ther1_cid, rgb1_cid, ther2_cid ,rgb2_cid, = 2,3,4,0
    print(f'after get ids, rgb_cid: {rgb1_cid}, ther_cid: {ther1_cid}')
    sleep(60)
    ther1_camera = cv2.VideoCapture(ther1_cid)
    rgb1_camera = cv2.VideoCapture(rgb1_cid,cv2.CAP_DSHOW)
    ther2_camera = cv2.VideoCapture(ther2_cid)
    rgb2_camera = cv2.VideoCapture(rgb2_cid,cv2.CAP_DSHOW)

    # output_dir
    dir_name=datetime.datetime.now().strftime('%Y%m%d')
    output_dir = "/Users/inet-lab/Desktop/mp4/" + dir_name + "/"
    if(not (os.path.exists(output_dir))):
        os.mkdir(output_dir)

    # 動画ファイル保存用の設定
    fps = 5
    #rgb_camera.set(cv2.CAP_PROP_FPS,fps)
    #ther_camera.set(cv2.CAP_PROP_FPS,fps)

    rgb1_w = int(rgb1_camera.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    ther1_w = int(ther1_camera.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    rgb1_h = int(rgb1_camera.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    ther1_h = int(ther1_camera.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')        # 動画保存時のfourcc設定（mp4用）
    strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M')
    rgb1_filename = output_dir + "rgb1_video" + strdate + ".mp4"
    ther1_filename = output_dir + "ther1_video" + strdate + ".mp4"
    rgb1_video = cv2.VideoWriter(rgb1_filename, fourcc, fps, (rgb1_w, rgb1_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
    ther1_video = cv2.VideoWriter(ther1_filename, fourcc, fps, (ther1_w, ther1_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）

    rgb2_w = int(rgb2_camera.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    ther2_w = int(ther2_camera.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    rgb2_h = int(rgb2_camera.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    ther2_h = int(ther2_camera.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    rgb2_filename = output_dir + "rgb2_video" + strdate + ".mp4"
    ther2_filename = output_dir + "ther2_video" + strdate + ".mp4"
    rgb2_video = cv2.VideoWriter(rgb2_filename, fourcc, fps, (rgb2_w, rgb2_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
    ther2_video = cv2.VideoWriter(ther2_filename, fourcc, fps, (ther2_w, ther2_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）


    # 10 minitesだけ処理を行う．
    looptime = 1
    dt_end = datetime.datetime.now() + datetime.timedelta(minutes=looptime)

    # 撮影＝ループ中にフレームを1枚ずつ取得（qキーで撮影終了）
    while(True):
        rgb1_ret, rgb1_frame = rgb1_camera.read()                             # フレームを取得
        rgb2_ret, rgb2_frame = rgb2_camera.read()                             # フレームを取得
        ther1_ret, ther1_frame = ther1_camera.read()                             # フレームを取得
        ther2_ret, ther2_frame = ther2_camera.read()                             # フレームを取得
        rgb1_video.write(rgb1_frame)                                     # 動画を1フレームずつ保存する
        rgb2_video.write(rgb2_frame)                                     # 動画を1フレームずつ保存する
        ther1_video.write(ther1_frame)                                     # 動画を1フレームずつ保存する
        ther2_video.write(ther2_frame)                                     # 動画を1フレームずつ保存する
        # キー操作があればwhileループを抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        sleep(1/fps)
        if dt_end < datetime.datetime.now():
            dt_end = dt_end + datetime.timedelta(minutes=looptime)
            strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M')
            rgb1_filename = output_dir + "rgb1_video" + strdate + ".mp4"
            rgb2_filename = output_dir + "rgb2_video" + strdate + ".mp4"
            ther1_filename = output_dir + "ther1_video" + strdate + ".mp4"
            ther2_filename = output_dir + "ther2_video" + strdate + ".mp4"
            rgb1_video = cv2.VideoWriter(rgb1_filename, fourcc, fps, (rgb1_w, rgb1_h))  
            rgb2_video = cv2.VideoWriter(rgb2_filename, fourcc, fps, (rgb2_w, rgb2_h))  
            ther1_video = cv2.VideoWriter(ther1_filename, fourcc, fps, (ther1_w, ther1_h))
            ther2_video = cv2.VideoWriter(ther2_filename, fourcc, fps, (ther2_w, ther2_h))
            print(f'create new file {dt_end}')


    # 撮影用オブジェクトとウィンドウの解放
    rgb1_camera.release()
    rgb2_camera.release()
    ther1_camera.release()
    ther2_camera.release()
    cv2.destroyAllWindows()
