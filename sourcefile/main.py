import tornado.ioloop
import tornado.web
import json
import os.path

from newExcuteFile import compute_risk_level

# static_path = os.path.join(os.path.dirname(__file__), "static")	
static_path = os.path.join(os.path.dirname(__file__), "../frontEnd/dist/")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # test = self.get_argument('test', '00')
        self.redirect('/static/index.html', permanent=True)
        # self.write(str(test))
    
    def post(self):
        data = self.request.body.decode('utf-8')
        data = json.loads(data)
        choice_arr = data['choice']
        risk_level = compute_risk_level(choice_arr)
        self.write(json.dumps({"data": risk_level}))

def make_app():
    return tornado.web.Application([
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": static_path}),
        (r"/compute_risk", MainHandler),
        (r"/", MainHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    # choice_arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # print(compute_risk_level(choice_arr))
