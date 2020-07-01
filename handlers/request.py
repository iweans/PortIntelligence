from tornado.web import RequestHandler
# --------------------------------------------------


class MainHandler(RequestHandler):

    def get(self):
        self.write("Hello, world")

        

class PedestrainDetHandler(RequestHandler):

    def get(self):
        self.write('Pedestrain Detection')
    
    def post(self):
        task_id = self.get_argument('tid')
        time_stamp = self.get_argument('timeStamp')
        cameraAddr = self.get_argument('cameraAddr')
        
        
        self.write('OK')



