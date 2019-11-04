import flask,json
from tools import my_db
server=flask.Flask(__name__)
@server.route('/',methods=['get'])
def index():
    res=my_db('select * from student')
    return json.dumps(res,ensure_ascii=True)
server.run(port=9999,debug=True,host='0.0.0.0')
print(server)
