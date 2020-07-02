import time
import requests
# ----------------------------------------
import configs
# --------------------------------------------------


URL_PATH = 'pedestrain'

start_time = time.time()
resp = requests.post(
    url=f'http://{configs.BIND_ADDR}:{configs.LISTEN_PORT}/{URL_PATH}',
    data={
        'taskId': '00001000',
        'action': 'prepare',
        'sendTime': time.time(),
        'cameraIp': '192.168.0.64',
        'cameraPort': 554,
        'cameraUser': 'admin',
        'cameraPass': 'a1234567',
        'cameraProtocol': 'rtsp',
        'cameraUriPath': 'MPEG-4/ch1/main/av_stream'
    }
)
end_time = time.time()
print(f'来回时间：{1000*(end_time-start_time)}ms')


print(resp.content)



