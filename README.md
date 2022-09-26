# バスの中に設置したNUC
NUC：

## Ubuntu Version
Ubuntu20.04
## Python Version
Python 

## Quick Start
```
pip3 install -r requirements.txt
```
定期実行のプログラムはcrontabで設定．
編集内容はcrontab-e.txtに記載．

/etc/systemd/system にファイルを追加
```cp /home/inet-lab/hogehoge/cap_rgb_video.service /etc/systemd/system/
cp /home/inet-lab/hogehoge/cap_ther_video.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl status
sudo systemctl enable
sudo systemctl start
```

## カメラの位置と撮影に関して
カメラは前後に設置されている．
そのため，RGBのカメラ撮影用とFIRカメラ撮影用のスクリプトを用意している．
systemdではそれぞれのスクリプトを動作させる．





