import threading
import time
import cv2
# ----------------------------------------
import configs.camera as camera_configs
# --------------------------------------------------


class LruCamera(threading.Thread):

    URI_TEMPLATE = "{camera_protocol}://{camera_user}:{camera_pass}@{camera_ip}:{camera_port}/{camera_uri_path}"

    def __init__(self, direct):
        ip = direct['camera_ip']
        super().__init__(daemon=True, name=ip)
        self._uri = self.parse_uri(direct)
        self._max_keep = camera_configs.MAX_KEEP
        self._max_continuous = camera_configs.MAX_CONTINUOUS
        self._lru_frames = []
        self._status = ''

    def run(self):
        cap = cv2.VideoCapture(self._uri)
        if not cap.isOpened():
            return False
        start_time = time.time()
        while True:
            current_time = time.time()
            if current_time - start_time > self._max_continuous:
                break

            


    @property
    def status(self):
        return self._status

    @classmethod
    def parse_uri(cls, direct):
        return cls.URI_TEMPLATE.format(direct)





