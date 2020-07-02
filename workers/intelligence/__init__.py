import multiprocessing
# --------------------------------------------------


class IntelligenceWorker(multiprocessing.Process):
    
    def __init__(self):
        super().__init__(daemon=True,
                         name='intelligence')
        
        self._direct_queue = multiprocessing.Queue()

    def run(self) -> None:
        from .main import Intelligence
        intelligence = Intelligence(self)
        intelligence()

    def put_direct(self, direct: str):
        self._direct_queue.put(direct)

    def get_direct(self) -> str:
        return self._direct_queue.get()

    def mount(self, app, point='intelligence'):
        setattr(app, point, self)

