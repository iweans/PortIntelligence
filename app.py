import tornado.ioloop
from tornado.web import Application
# ----------------------------------------
from workers import IntelligenceWorker
from handlers.request import MainHandler, PedestrainDetHandler
import configs
# --------------------------------------------------


intelligence = IntelligenceWorker()
intelligence.start()


app = tornado.web.Application([
    (r'/', MainHandler),
    (r'/pedestrain', PedestrainDetHandler)
], debug=configs.DEBUG)
intelligence.mount(app)


if __name__ == "__main__":
    app.listen(port=configs.LISTEN_PORT, address=configs.BIND_ADDR)
    print(f'Tornado listen on {configs.LISTEN_PORT} ...')
    tornado.ioloop.IOLoop.current().start()
