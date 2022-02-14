from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import *
from gevent import pywsgi
from flask_cors import cross_origin
# from flask_json import as_json
from flask_cors import CORS

app = Flask(__name__, static_url_path='/', static_folder='./../../flask-dist', template_folder='./../../flask-dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://你的数据库账号:你的数据库密码@数据库ip:数据库端口/数据库名称'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 如果设置成True(默认情况)，Flask - SQLAlchemy将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_UCSO'] = True
CORS(app, supports_credentials=True)
# 声明数据对象
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


# 查询数据的接口
# @as_json
@app.route('/getUser', methods=['GET', 'POST'])
def get_user():
    res = db.session.query(Yiqing).all()  # Yiqing是从models里导入的
    temp = []
    for x in res:
        temp.append(x.to_json())
    return jsonify(data=temp)


# 新增数据的接口
@cross_origin(supports_credentials=True)
@app.route('/addUser', methods=['POST'])
def add_user():
    # data = request.json(force=True)  # 获取传过来的参数
    # data = request.get_json()  # 获取传过来的参数

    data = request.form.to_dict()  # 获取传过来的参数
    print(data)
    # data = jsonify(data)
    # print(data)
    u = Yiqing(user=data.get("user"), password=data.get("password"))  # 根据传过来参数创建一条数据
    db.session.add(u)  # add 是增加数据
    db.session.commit()  # 提交了才会到数据库中
    return 'success', 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()
