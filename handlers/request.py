import time
# ----------------------------------------
from tornado.web import RequestHandler
# --------------------------------------------------


class MainHandler(RequestHandler):

    async def get(self):
        self.write("Hello, world")


class PedestrainDetHandler(RequestHandler):

    async def get(self):
        self.write('Pedestrain Detection')

    async def post(self):
        recv_time = time.time()
        content_type = self.request.headers.get('Content-Type')

        if 'form' in content_type:
            self.application.intelligence.put_direct({
                'task_type': 'pedestrain_det',
                'task_id': self.get_argument('taskId'),
                'action': self.get_argument('action'),
                'send_time': float(self.get_argument('sendTime')),
                'recv_time': recv_time,
                'camera_ip': self.get_argument('cameraIp'),
                'camera_port': int(self.get_argument('cameraPort')),
                'camera_user': self.get_argument('cameraUser'),
                'camera_pass': self.get_argument('cameraPass'),
                'camera_protocol': self.get_argument('cameraProtocol'),
                'camera_uri_path': self.get_argument('cameraUriPath'),
            })
        else:
            pass

        self.write('OK')

