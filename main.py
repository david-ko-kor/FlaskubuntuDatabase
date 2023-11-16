from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
app = Flask(__name__)
# app.config['SECRET_KEY'] ='1234'
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# engine = create_engine('postgresql://postgres:1234@localhost/mydatabase')
#
# # 연결
# with engine.connect() as connection:
#     # 여기에 원하는 작업을 수행합니다.
#     result = connection.execute("SELECT 1")
#     print(result.fetchone())
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age=db.Column(db.Integer)

@app.route('/')
def index():
    user =User(name='goremi',age=41)
    print(user.name)

    return  'ok'
if __name__ == '__main__':
    app.run(debug=True,port=8000)