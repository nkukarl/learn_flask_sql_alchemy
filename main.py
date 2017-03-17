from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:////Users/kwang/PycharmProjects/learn_flask_sql_alchemy/example.db'
db = SQLAlchemy(app)

db.create_all()