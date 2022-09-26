#!/bin/bash
/usr/bin/sleep 10 &&
/usr/bin/systemctl start cap_video.service &&
/usr/bin/sleep 10 &&
/usr/bin/systemctl stop cap_video.service &&
/usr/bin/sleep 10 &&
/usr/bin/systemctl start cap_video.service



