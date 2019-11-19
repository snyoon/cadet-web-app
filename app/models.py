from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    usertype = db.Column(db.String(64))
    uniformscores = db.relationship('UniformScore', backref='cadet', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_usertype(self, accounttype):
        if (accounttype == 'o'):
            self.usertype = 'Officer'
        else:
            self.usertype = 'Cadet'


class UniformScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    week1score = db.Column(db.Integer, default=0)
    week2score = db.Column(db.Integer, default=0)
    week3score = db.Column(db.Integer, default=0)
    week4score = db.Column(db.Integer, default=0)
    week5score = db.Column(db.Integer, default=0)
    week6score = db.Column(db.Integer, default=0)
    week7score = db.Column(db.Integer, default=0)
    week8score = db.Column(db.Integer, default=0)
    week9score = db.Column(db.Integer, default=0)
    week10score = db.Column(db.Integer, default=0)
    week11score = db.Column(db.Integer, default=0)
    week12score = db.Column(db.Integer, default=0)
    week13score = db.Column(db.Integer, default=0)
    week14score = db.Column(db.Integer, default=0)
    week15score = db.Column(db.Integer, default=0)
    week16score = db.Column(db.Integer, default=0)
    week17score = db.Column(db.Integer, default=0)
    week18score = db.Column(db.Integer, default=0)
    week19score = db.Column(db.Integer, default=0)
    week20score = db.Column(db.Integer, default=0)
    week21score = db.Column(db.Integer, default=0)
    week22score = db.Column(db.Integer, default=0)
    week23score = db.Column(db.Integer, default=0)
    week24score = db.Column(db.Integer, default=0)
    week25score = db.Column(db.Integer, default=0)
    week26score = db.Column(db.Integer, default=0)
    week27score = db.Column(db.Integer, default=0)
    week28score = db.Column(db.Integer, default=0)
    week29score = db.Column(db.Integer, default=0)
    week30score = db.Column(db.Integer, default=0)
    week31score = db.Column(db.Integer, default=0)
    week32score = db.Column(db.Integer, default=0)
    week33score = db.Column(db.Integer, default=0)
    week34score = db.Column(db.Integer, default=0)
    week35score = db.Column(db.Integer, default=0)
    week36score = db.Column(db.Integer, default=0)
    week37score = db.Column(db.Integer, default=0)
    week38score = db.Column(db.Integer, default=0)
    week39score = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<UniformScores {}>'.format(self.body)

    def set_score(self, week, score):
        appendedWord = 'week' + str(week) + 'score'
        setattr(self, appendedWord, score)


class PerformanceCheckScores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    score1 = db.Column(db.Integer)
    score2 = db.Column(db.Integer)
    score3 = db.Column(db.Integer)
    score4 = db.Column(db.Integer)
    score5 = db.Column(db.Integer)
    score6 = db.Column(db.Integer)
    score7 = db.Column(db.Integer)
    score8 = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<PerformanceCheckSCores {}>'.format(self.body)

    def set_score(self, week, score):
        appendedWord = 'score' + str(week)
        setattr(self, appendedWord, score)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))