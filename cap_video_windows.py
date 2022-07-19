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
    for id in range(0,10):
        capid=cv2.VideoCapture(id, cv2.CAP_DSHOW)
        if capid.isOpened():
            print(capid.get(cv2.CAP_PROP_FRAME_HEIGHT))
            if capid.get(cv2.CAP_PROP_FRAME_HEIGHT)==122:
                ther_cid=id
            elif capid.get(cv2.CAP_PROP_FRAME_HEIGHT)==360:
                rgb_cid=id
            # print(f'Video capture{id}:found')
        else:
            print(f'Video capture{id}:None')
        capid.release()

    print(f'after get ids, rgb_cid: {rgb_cid}, ther_cid: {ther_cid}')
    sleep(60)
    ther_camera = cv2.VideoCapture(ther_cid)
    rgb_camera = cv2.VideoCapture(rgb_cid,cv2.CAP_DSHOW)

    # output_dir
    dir_name=datetime.datetime.now().strftime('%Y%m%d')
    output_dir = "/Users/inet-lab/Desktop/mp4/" + dir_name + "/"
    if(not (os.path.exists(output_dir))):
        os.mkdir(output_dir)

    # 動画ファイル保存用の設定
    fps = 9

    rgb_w = int(rgb_camera.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    ther_w = int(ther_camera.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    rgb_h = int(rgb_camera.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    ther_h = int(ther_camera.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')        # 動画保存時のfourcc設定（mp4用）
    strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M')
    rgb_filename = output_dir + "rgb_video" + strdate + ".mp4"
    ther_filename = output_dir + "ther_video" + strdate + ".mp4"
    rgb_video = cv2.VideoWriter(rgb_filename, fourcc, fps, (rgb_w, rgb_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
    ther_video = cv2.VideoWriter(ther_filename, fourcc, fps, (ther_w, ther_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）

    # 10 minitesだけ処理を行う．
    looptime = 1
    dt_end = datetime.datetime.now() + datetime.timedelta(minutes=looptime)

    # 撮影＝ループ中にフレームを1枚ずつ取得（qキーで撮影終了）
    while(True):
        rgb_ret, rgb_frame = rgb_camera.read()                             # フレームを取得
        ther_ret, ther_frame = ther_camera.read()                             # フレームを取得
        rgb_video.write(rgb_frame)                                     # 動画を1フレームずつ保存する
        ther_video.write(ther_frame)                                     # 動画を1フレームずつ保存する
        # キー操作があればwhileループを抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        sleep(1/fps)
        if dt_end < datetime.datetime.now():
            dt_end = dt_end + datetime.timedelta(minutes=looptime)
            strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M')
            rgb_filename = output_dir + "rgb_video" + strdate + ".mp4"
            ther_filename = output_dir + "ther_video" + strdate + ".mp4"
            rgb_video = cv2.VideoWriter(rgb_filename, fourcc, fps, (rgb_w, rgb_h)) 
            ther_video = cv2.VideoWriter(ther_filename, fourcc, fps, (ther_w, ther_h))
            print(f'create new file {dt_end}')


    # 撮影用オブジェクトとウィンドウの解放
    rgb_camera.release()
    ther_camera.release()
    cv2.destroyAllWindows()
