import tornado.ioloop
import tornado.web
import json

from newExcuteFile import compute_risk_level

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        test = self.get_argument('test', '00')
        self.write(str(test))
    
    def post(self):
        data = self.request.body.decode('utf-8')
        data = json.loads(data)
        choice_arr = data['choice']
        print(type(choice_arr))
        # self.write(json.dumps(choice_arr))
        risk_level = compute_risk_level(choice_arr)

        self.write(json.dumps(risk_level))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    # choice_arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # print(compute_risk_level(choice_arr))
