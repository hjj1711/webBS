from flask import Flask,render_template
import json
import  decimal
from sqlalchemy.ext.declarative import DeclarativeMeta
import datetime
app = Flask(__name__)

from flask import Flask, jsonify, request,render_template,url_for,redirect,session
from mysql import db, app, Qoutes
@app.route('/',methods=['GET', 'POST'])
def hello_world():
    return "hello world"
@app.route('/test', methods=['GET', 'POST'])
def test():
    qoutes=Qoutes.query.all()
    for q in qoutes:
        app.logger.debug(q.times)
        times=q.times#日期
        op=q.OP#开盘价
        cp = q.CP # 收盘价
        lp = q.LP  # 最低价
        hp=q.HP#最高价

    # return "%s %d" % (times,op)
    # return render_template('index.html', times=times,op=op,hp=hp,lp=lp,cp=cp)
    #return render_template('index.html',qoutes=jsonify(q))
    return render_template('index.html',qoutes=qoutes,times=times,op=op,cp=cp,lp=lp,hp=hp)

@app.route('/test2', methods=['GET', 'POST'])
def test2():
    #if request.method == "GET":
    qoutes = Qoutes.query.all()
    #q=qoutes.to_dict()
    # for q in qoutes:
    #     app.logger.debug(q.times)
    #     times=q.times#日期
    #     op=q.OP#开盘价
    #     cp = q.CP # 收盘价
    #     lp = q.LP  # 最低价
    #     hp=q.HP#最高价
    ql=[]
    for q in qoutes:
        ql.append(q)


    return json.dumps(ql, cls=AlchemyEncoder, check_circular=False)




#对时间与数字的数据格式进行转换，方便python的json序列化
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)     # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:    # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    elif isinstance(data, decimal.Decimal):
                        fields[field] = data.__float__()
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields

@app.route('/plotly', methods=['GET', 'POST'])
def plotly():
    qoutes = Qoutes.query.all()
    ql = []
    for q in qoutes:
        ql.append(q)
    return render_template('index.html', data=json.dumps(ql, cls=AlchemyEncoder, check_circular=False))


# 对时间与数字的数据格式进行转换，方便python的json序列化
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:  # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    elif isinstance(data, decimal.Decimal):
                        fields[field] = data.__float__()
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields

@app.route('/testx', methods=['GET', 'POST'])
def testx():
    qoutes = Qoutes.query.all()
    ql = []
    for q in qoutes:
        ql.append(q)
    return render_template('testx.html',data=json.dumps(ql, cls=AlchemyEncoder, check_circular=False))
#对时间与数字的数据格式进行转换，方便python的json序列化
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)     # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:    # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    elif isinstance(data, decimal.Decimal):
                        fields[field] = data.__float__()
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields
if __name__ == '__main__':
    app.run()
