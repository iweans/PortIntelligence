import time
import cv2
# --------------------------------------------------


class Intelligence(object):

    def __init__(self, worker):
        self._worker = worker

    def __call__(self):
        while True:
            direct = self._worker.get_direct()

            camera_uri = f"{direct['camera_protocol']}://" \
                         f"{direct['camera_user']}:" \
                         f"{direct['camera_pass']}@" \
                         f"{direct['camera_ip']}:" \
                         f"{direct['camera_port']}/" \
                         f"{direct['camera_uri_path']}"

            start_time = time.time()
            cap = cv2.VideoCapture(camera_uri)
            if not cap.isOpened():
                print('摄像头连接失败！')
                exit()
            end_time = time.time()
            print(f'连接摄像头延时: {1000 * (end_time - start_time):.4f} ms')


            # current_time = time.time()
            # send_time = direct['send_time']
            # recv_time = direct['recv_time']
            #
            # print(f'HTTP延时: {1000*(recv_time-send_time)}ms')
            # print(f'Process通信延时: {1000*(current_time-recv_time)}ms')
            # print(f'[Direct] {direct}')



