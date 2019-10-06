# -*- coding:utf-8 -*-



import tornado.ioloop
import tornado.web
import json
import os.path

from newExcuteFile import compute_by_config
import sys
sys.path.append("../")
from controlmodules.ReadConfig import readIndex
from controlmodules.RiskManagement import index_management
from controlmodules.RiskManagement import send_management


# static_path = os.path.join(os.path.dirname(__file__), "static")
static_path = os.path.join(os.path.dirname(__file__), "../frontEnd/dist/")



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('/static/index.html', permanent=True)

    def post(self):
        # achieve each risk level
        data = self.request.body.decode('utf-8')
        data = json.loads(data)
        choice_arr = data['choice']
        print choice_arr
        risk_level = compute_by_config(choice_arr)
        self.write(json.dumps({"data": risk_level}))

class IndexHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def get(self):
        # achive all risk indexes
        risk_indexes = readIndex()[0]
        # risk_indexes = ['无法联系','有人']
        data = {
            "risk_indexes": risk_indexes
        }
        self.write(json.dumps(data))

    def post(self):
        # add risk index
        data = self.request.body.decode('utf-8')
        data = json.loads(data)
        category = data['category']
        name = data['name']
        impact = data['impact']
        probability = data['probability']
        index_management(category, name, impact, probability)

class AlarmHandler(tornado.web.RequestHandler):
    def post(self):
        # add risk index
        data = self.request.body.decode('utf-8')
        data = json.loads(data)
        level = data['level']
        isSend = data['isSend']
        receiver = data['receiver']
        send_management(level, isSend, receiver)

def make_app():
    return tornado.web.Application([
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": static_path}),
        (r"/compute_risk", MainHandler),
        (r"/indexes", IndexHandler),
        (r"/alarms", IndexHandler),
        (r"/", MainHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()
    print "start"
    # choice_arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # print(compute_risk_level(choice_arr))
