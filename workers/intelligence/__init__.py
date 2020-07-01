import multiprocessing
# --------------------------------------------------


class IntelligenceWorker(multiprocessing.Process):
    
    def __init__(self):
        super().__init__(daemon=True,
                         name='intelligence')
        
        self._direct_queue = multiprocessing.Queue()

    def run(self) -> None:
        while True:
            direct = self._direct_queue.get()
            print(f'[Direct] {direct}')


    def put_direct(self, direct: str) -> bool:
        try:
            self._direct_queue.put(direct)
            return True
        except:
            return False

