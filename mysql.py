# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 0018 16:02
# @Author  : HJ
# @Email   : 18287251710@163.com
# @File    : mysql.py
# @Software: JetBrains PyCharm 2018.1.2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date,DECIMAL
import config
import json
import  decimal
from sqlalchemy.ext.declarative import DeclarativeMeta
import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

class Qoutes(db.Model):
    __tablename__ = 'qoutes'

    times = db.Column('times', Date, primary_key=True)#日期
    OP = db.Column('OP', DECIMAL(65,2), unique=False)#开盘价
    HP = db.Column('HP', DECIMAL(65, 2), unique=False)#最高价
    LP = db.Column('LP', DECIMAL(65, 2), unique=False)#最低价
    CP = db.Column('CP', DECIMAL(65, 2), unique=False)#收盘价
    UD = db.Column('UD', DECIMAL(65, 2), unique=False)#涨跌额
    RF = db.Column('RF', DECIMAL(65, 2), unique=False)#涨跌幅(%)
    turnover = db.Column('turnover', DECIMAL(65, 2), unique=False)#成交量(手)
    TV = db.Column('TV', DECIMAL(65, 2), unique=False)#成交金额(万元)

    # 你 def __init__(self, times=None,OP=None,HP=None,LP=None,CP=None,UD=None,RF=None,turnover=None,TV=None):
    #     self.playerid = date
    #     self.userid = OP
    #     self.username = HP
    #     self.email = LP
    #     self.userage= CP
    #     self.userage = UD
    #     self.userage = RF
    #     self.userage = turnover
    #     self.userage = TV
    # def __repr__(self):
    #     return '<Qoutes %s %f %f %f %f %f %f %f %f>' % (self.date,self.OP,self.HP,self.LP,self.CP,self.UD,self.RF,self.turnover,self.TV)


#     #test3转化json测试
#     def to_json(self):
#         json_data = {
#             "times": self.times,
#             "values":[
#                 self.OP,
#                 self.CP,
#                 self.LP,
#                 self.HP
#             ]
#         }
#         return json.dumps(json_data, cls=AlchemyEncoder, check_circular=False)
#
# # class DateEncoder(json.JSONEncoder):
# #     def default(self,obj):
# #         if isinstance(obj, datetime.datetime):
# #             return obj.strftime(datetime)
# #         elif isinstance(obj,datetime.date):
# #             return obj.strftime(datetime)
# #         elif isinstance(obj,decimal):
# #             return str(obj)
# #         else:
# #             return json.JSONEncoder.default(self,obj)
# class AlchemyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj.__class__, DeclarativeMeta):
#             # an SQLAlchemy class
#             fields = {}
#             for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
#                 data = obj.__getattribute__(field)
#                 try:
#                     json.dumps(data)     # this will fail on non-encodable values, like other classes
#                     fields[field] = data
#                 except TypeError:    # 添加了对datetime的处理
#                     if isinstance(data, datetime.datetime):
#                         fields[field] = data.isoformat()
#                     elif isinstance(data, datetime.date):
#                         fields[field] = data.isoformat()
#                     elif isinstance(data, datetime.timedelta):
#                         fields[field] = (datetime.datetime.min + data).time().isoformat()
#                     elif isinstance(data, decimal.Decimal):
#                         fields[field] = data.__float__()
#                     else:
#                         fields[field] = None
#             # a json-encodable dict
#             return fields
if __name__ == '__main__':
    db.create_all()