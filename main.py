import cv2
import glob
import datetime
import settings

if __name__ == '__main__':

    files = glob.glob(settings.path)

    video_len_sec = 0

    for file in files:
        print(file)
        file_name = file
        cap = cv2.VideoCapture(file_name)                  
        video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        video_fps = cap.get(cv2.CAP_PROP_FPS)
        video_len_sec += video_frame_count / video_fps

    print('合計', datetime.timedelta(seconds=int(video_len_sec)))