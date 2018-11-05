from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignment.sqlite'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Assignment(db.Model):

    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True)
    assignmtInfo = db.Column(db.String(200), nullable=False)
    assignmtClass = db.Column(db.String(100), nullable=False)
    #assignmtDate = db.Column(db.String(200), nullable=False)
    assignmtDate = db.Column(db.Date(), nullable=False)

    def __repr__(self):
        return '<Assignments %r>' % self.assignmtClass
