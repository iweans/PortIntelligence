import multiprocessing
# --------------------------------------------------


class IntelligenceWorker(multiprocessing.Process):
    
    def __init__(self):
        super().__init__(daemon=True,
                         name='intelligence')
        
        self._direct_queue = multiprocessing.Queue()

    def run(self) -> None:
        import time
        while True:
            direct = self._direct_queue.get()
            current_time = time.time()
            send_time = direct['send_time']
            recv_time = direct['recv_time']

            print(f'HTTP延时: {1000*(recv_time-send_time)}ms')
            print(f'Process通信延时: {1000*(current_time-recv_time)}ms')
            # print(f'[Direct] {direct}')

    def put_direct(self, direct: str) -> bool:
        try:
            self._direct_queue.put(direct)
            return True
        except:
            return False

    def mount(self, app, point='intelligence'):
        setattr(app, point, self)

