import tornado.ioloop
import tornado.web
import json
# 引入一个函数，
# from newExcuteFile import compute_risk_level

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        test = self.get_argument('test', '00')
        self.write(str(test))
    
    def post(self):
        data = self.request.body.decode('utf-8')
        data = json.loads(data)
        choice_arr = data['choice']
        # risk_level = compute_risk_level(choice_arr)
        print(type(choice_arr))
        self.write(json.dumps(choice_arr))
        # self.write(json.dumps(risk_level))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler), # urlSpec Dict或truple
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start() # 样板代码