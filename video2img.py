# coding=utf-8
import cv2
import os

path = '/Users/frandy/LearnSpace/python/deep_learning/gauze/videos'
video_list = os.listdir(path)
for video in video_list:
    video_path = os.path.join(os.getcwd(), path, video)
    vc = cv2.VideoCapture(video_path)
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    c = 1
    i = 0
    Num_Threshold = 30
    while rval:
        rval, frame = vc.read()
        i += 1
        if i % Num_Threshold == 0:
            cv2.imwrite('/Users/frandy/LearnSpace/python/deep_learning/gauze/images/' + str(video) + str(c) + '.jpg',
                        frame)
            i = 0
        print(c)
        c = c + 1
        cv2.waitKey(1)
    vc.release()
