#!/bin/bash

# rsync -ahv /home/pi/work/mp4 rsh:/home/is/takumi-fu/2022_camera_data
rsync -ahvu /home/inet-lab/minato_camera_in_bus/mp4 rsh:/project/inet-its/2022-image-in-bus
find  /home/inet-lab/minato_camera_in_bus/mp4/ -mtime +60 -exec rm {} \;
