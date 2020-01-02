from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class UniformScoreSubmission(FlaskForm):
    week = StringField('Week', validators=[DataRequired()])
    score = StringField('Score', validators=[DataRequired()])
    cadet_last_name = StringField('Cadet Last Name', validators=[DataRequired()])
    cadet_first_name = StringField('Cadet First Name', validators=[DataRequired()])
    submit = SubmitField('Enter Score')

class PerformanceScoreForm(FlaskForm):
    cadet_last_name = StringField('Cadet Last Name', validators=[DataRequired()])
    cadet_first_name = StringField('Cadet First Name', validators=[DataRequired()])
    score = StringField('Score', validators=[DataRequired()])
    performance = SelectField(u'Performance Check', choices=[('score1', 'score1'), ('score2', 'score2'),
                                                             ('score3', 'score3'), ('score4', 'score4'),
                                                             ('score5', 'score5'), ('score7', 'score7'),
                                                             ('score6', 'score6'), ('score8', 'score8')])
    submit = SubmitField('Enter Score')
