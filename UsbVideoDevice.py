from curses.ascii import US
from dataclasses import replace
from ipaddress import v4_int_to_packed
from select import select
import subprocess

class UsbVideoDevice():
    def __init__(self):
        self.__deviceList = []

        try:
            cmd = '/usr/bin/v4l2-ctl --list-devices'
            res = subprocess.check_output(cmd.split())
            v4l2_ctl = res.decode()
            # print(v4l2_ctl)        
        except:
            return

        # try:
        #     cmd = 'ls -la /dev/v4l/by-path'
        #     res = subprocess.check_output(cmd.split())
        #     by_path = res.decode()
        # except:
        #     return

        # デバイス名取得
        line_counter=1
        front_rgb_line=0
        rear_rgb_line=0
        front_ther_line=0
        rear_ther_line=0

        # ポート番号取得
        for line in v4l2_ctl.split('\n'):
            if('HD USB Camera' in line and '.0-1.' in line): #RGBカメラandフロント
                front_rgb_line=line_counter                
            elif('HD USB Camera' in line and '.0-2.' in line): #RGBカメラandリア
                rear_rgb_line=line_counter                
            elif('PureThermal' in line and '.0-1.' in line): #Thermalカメラandフロント
                front_ther_line=line_counter                
            elif('PureThermal' in line and '.0-2.' in line): #Thermalカメラandリア
                rear_ther_line=line_counter                
            line_counter += 1
        # print(front_rgb_line,rear_rgb_line,front_ther_line,rear_ther_line)


        # ポート番号取得
        line_counter=1
        for line in v4l2_ctl.split('\n'):
            #front_rgb
            if front_rgb_line+1==line_counter:
                tmp = self.__split(line, '/dev/video')
                deviceId = int(tmp[1])
                self.__deviceList.append(('front_rgb', deviceId))    

            #rear_rgb
            elif rear_rgb_line+1==line_counter:
                tmp = self.__split(line, '/dev/video')
                deviceId = int(tmp[1])
                self.__deviceList.append(('rear_rgb', deviceId))    

            #front_ther
            elif front_ther_line+1==line_counter:
                tmp = self.__split(line, '/dev/video')
                deviceId = int(tmp[1])
                self.__deviceList.append(('front_ther', deviceId))    

            #rear_ther
            elif rear_ther_line+1==line_counter:
                tmp = self.__split(line, '/dev/video')
                deviceId = int(tmp[1])
                self.__deviceList.append(('rear_ther', deviceId))    

            line_counter += 1

#                tmp = self.__split(tmp[1], ':')
#                 port = int(tmp[0])
#                 tmp = self.__split(tmp[1], '../../video')
#                 deviceId = int(tmp[1])
#                 if deviceId % 2 == 0:
#                     name = deviceNames[str(deviceId)]
#                     self.__deviceList.append(("front", deviceId , port, name))
# 
    def __split(self, str, val):
        tmp = str.split(val)
        if('' in tmp):
            tmp.remove('')
        return tmp

    # 認識しているVideoデバイスの一覧を表示する
    def disp(self):
        for (name, deviceId) in self.__deviceList:
            print("{} /dev/video{}".format(name, deviceId))


    def getdevicelist(self):
        print(self.__deviceList)
        return self.__deviceList

'''
    # ポート番号（1..）を指定してVideoIDを取得する
    def getId(self, port):
        for (_, deviceId, p, _) in self.__deviceList:
            if(p == port):
                return deviceId
        return -1

'''

# if __name__ == '__main__':
    # UsbVideoDevice().getdevicelist()