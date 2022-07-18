# minato_camera_in_bus

## 当日
powershell を使って起動
python3.10のインストール(pwershellで`python3`と実行するとinstallの画面に変移する)

```python3 -m venv .venv
.venv/Scripts/activate.bat //起動
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force //最初だけこのスクリプトが必要
.venv\Scripts\activate.ps1 //起動
python3 -m pip install opencv-python
python3 -m pip install opencv-contrib-python
```
もしくはrequirements.txtのインストール

## スクリプトの自動起動に関して
Windows標準のタスクスケジューラを利用（Winキー+S）
基本タスクを作成する
- 名前：適当だけどファイル名の方がいいかも
- コンピュータの起動時に実行
- プログラムの開始
- pythonまでのパスはvenv環境のもの
- 引数としてファイルのパスを指定

### ユーザがログオンしてないときにも実行
タスクスケジューラからタスクをダブルクリック
「ログオンしているかどうかに関わらず実行する」を選択する
タスクが失敗したときの対応→1分ごとに10回試行






