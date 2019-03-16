# from
# from flask import Flask, jsonify, request,render_template,url_for,redirect,session
# from mysql import db, app, Player
# import redis
# @app.route('/')
# def log():
#     return redirect(url_for('login'))
#
# @app.route('/index')
# def index():
#     return redirect(url_for('list_players'))
# #登录
# @app.route("/login",methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         p_username = request.form.get('username',None)
#         p_userpwd = request.form.get('userpwd',None)
#         if not p_username or not p_userpwd:
#             return '请输入姓名和密码'
#         player = Player.query.filter_by(username=p_username,pwd=p_userpwd).all()
#         for p in player:
#             if p:
#                 return redirect(url_for('index'))
#             else:
#                 return "姓名或密码错误"
#     return render_template('login.html')
# #显示所有数据
# @app.route('/show')
# def list_players():
#     players = Player.query.all()
#     return render_template('show.html',player=players)
# #显示最后一条数据
# @app.route('/showlast')
# def list_players2():
#     players = Player.query.all()
#     for p in players:
#         app.logger.debug(p.username)
#         a = p.username
#         b = p.email
#         c = p.playerid
#         d = p.userage
#     return "你好: %s，你的邮箱号为：%s，你的编号为：%d，你的年龄为：%d " % (a,b,c,d)
# #添加数据
# @app.route('/add/1', methods=['GET', 'POST'])
# def add():
#     if request.method == 'POST':
#         #p_playerid = request.form.get('playerid',None)
#         p_userid = request.form.get('userid',None)
#         p_username = request.form.get('username',None)
#         p_email = request.form.get('email', None)
#         p_userage = request.form.get('userage', None)
#
#         if not p_userid or not p_username or not p_email or not p_userage:
#             return '请输入完整的信息'
#
#         newobj = Player(userid=p_userid, username=p_username, email=p_email, userage=p_userage)
#         db.session.add((newobj))
#         db.session.commit()
#         players = Player.query.all()
#         return render_template('add.html', players=players)
#     players = Player.query.all()
#     return render_template('add.html', players=players)
# #带条件的查询
# @app.route('/que',methods=['GET','POST'])
# def que():
#     if request.method == 'POST':
#         p_userid = request.form.get('userid',None)
#         p_username = request.form.get('username',None)
#         #组合式查询
#         if not p_userid or not p_username:
#             if not p_userid and not p_username:
#                 players = Player.query.all()
#                 return render_template('que.html', players=players)
#             elif not p_userid:
#                 players = Player.query.filter_by(username=p_username).all()
#                 return render_template('que.html', players=players)
#             elif not p_username:
#                 players = Player.query.filter_by(userid=p_userid).all()
#                 return render_template('que.html', players=players)
#         else:
#             players = Player.query.filter_by(userid=p_userid,username=p_username).all()
#             return render_template('que.html', players=players)
#     players = Player.query.all()
#     return render_template('que.html', players=players)
#
# #删除数据
# @app.route('/delx/<playerid>',methods=['GET','POST'])
# def delx(playerid):
#     players=Player.query.get(playerid)
#     if players:
#         try:
#             db.session.delete(players)
#             db.session.commit()
#         except Exception:
#
#             print('删除信息失败')
#             db.session.rollback()
#     else:
#         print('未找到信息')
#     return redirect(url_for('list_players'))
#
#
#
# #修改数据
# @app.route('/update/<playerid>',methods=['GET','POST'])
# def update(playerid):
#     r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
#     r.set('id1', playerid)
#     a = r.get('id1')
#     return redirect(url_for('update1'))
#
#
# @app.route('/update/',methods=['GET','POST'])
# def update1():
#     r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
#     a = r.get('id1')
#     if request.method == 'GET':
#         #players = Player.query.filter(Player.playerid == a).first()
#         players = Player.query.filter_by(playerid=a).all()
#         return render_template('update.html', players=players )
#     else:
#         p_userid = request.form.get('userid', None)
#         p_username = request.form.get('username', None)
#         p_email = request.form.get('email', None)
#         p_userage = request.form.get('userage', None)
#         players = Player.query.filter(Player.playerid == a).first()
#         players.userid = p_userid
#         players.username = p_username
#         players.email = p_email
#         players.userage = p_userage
#         db.session.commit()
#         return redirect(url_for('list_players'))
#
#
# @app.route('/redis')
# def getredis():
#     r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
#     a = r.get('id1')
#     return a
#
#
#
#
# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='0.0.0.0',port=5000)