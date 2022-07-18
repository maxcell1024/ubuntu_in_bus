import cv2

# 画像ファイルの読み込み(カラー画像(3チャンネル)として読み込まれる)
img = cv2.imread("test.jpg")

# 画像の表示
cv2.imshow("Image", img)

# キー入力待ち(ここで画像が表示される)
cv2.waitKey()