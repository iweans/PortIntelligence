import cv2
import time


CAMERA_USER = 'admin'
CAMERA_PASS = 'a1234567'
CAMERA_IP = '192.168.0.64'
CAMERA_PORT = 554

CAMERA_URI = f'rtsp://{CAMERA_USER}:{CAMERA_PASS}@{CAMERA_IP}:{CAMERA_PORT}/MPEG-4/ch1/main/av_stream'

start_time = time.time()
cap = cv2.VideoCapture(CAMERA_URI)
if not cap.isOpened():
    print('摄像头连接失败！')
    exit()
end_time = time.time()
print(f'连接摄像头延时: {1000*(end_time-start_time)}ms')


start_time = time.time()
if not cap.isOpened():
    print('摄像头连接失败！')
    exit()
end_time = time.time()
print(f'测试连接状态延时: {1000*(end_time-start_time)}ms')


start_time = time.time()
# cv2.namedWindow('frame')
frame_count = 0
while True:
    ret_val, frame = cap.read()
    if not ret_val:
        print('摄像头丢失')
        break

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    frame_count += 1
    if frame_count == 100:
        break
    # cv2.imshow('frame', frame)
    # cv2.waitKey(1)
end_time = time.time()
print(f'elapsed time: {end_time-start_time:.2f}s ({10*(end_time-start_time):.4f}ms)')


cap.release()
del cap
