#!/usr/bin/python
# -*- coding: utf-8 -*-

import screeninfo

BigB_X = 180
BigB_Y = 50

try:
    monitor_width = screeninfo.get_monitors()[0].width
    monitor_height = screeninfo.get_monitors()[0].height

    X_Size = int(monitor_width//1.5) # 1280
    Y_Size = int(monitor_height//1.5) # 720
    screen_pos_x = monitor_width // 2 - X_Size // 2  # 320
    screen_pos_y = monitor_height // 2 - Y_Size // 2  # 180
except:
    X_Size = 1280
    Y_Size = 720
    screen_pos_x = 1980 // 2 - X_Size // 2  # 320
    screen_pos_y = 1080 // 2 - Y_Size // 2  # 180

