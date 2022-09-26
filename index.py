import cv2
from UsbVideoDevice import UsbVideoDevice

usbVideoDevice = UsbVideoDevice()

print("情報一覧")
usbVideoDevice.disp()

# print("\nポート番号とデバイスIDの一覧")
# for port in range(4):
#     deviceId = usbVideoDevice.getId(port + 1)
#     if (deviceId != -1):
#         print("PORT:{} /dev/video{}".format(port + 1, deviceId))