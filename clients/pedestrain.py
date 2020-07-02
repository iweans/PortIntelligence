import time
import requests
# ----------------------------------------
import configs
# --------------------------------------------------


URL_PATH = 'pedestrain'

resp = requests.post(
    url=f'http://{configs.BIND_ADDR}:{configs.LISTEN_PORT}/{URL_PATH}',
    data={
        'taskId': '00001000',
        'sendTime': time.time(),
        'cameraIp': '192.168.0.64',
        'cameraPort': 80,
        'cameraUser': 'admin',
        'cameraPass': 'a1234567',
        'cameraProtocol': 'rtsp',
        'cameraUriPath': 'video'
    }
)


print(resp.content)



