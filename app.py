import tornado.ioloop
from tornado.web import Application
# ----------------------------------------
from workers import IntelligenceWorker
from handlers.request import MainHandler
import configs
# --------------------------------------------------





app = tornado.web.Application([
    (r'/', MainHandler),
])


if __name__ == "__main__":
    app.listen(configs.LISTEN_PORT)
    tornado.ioloop.IOLoop.current().start()
