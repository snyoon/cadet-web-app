from flask import render_template, flash, redirect, url_for, request
from app import app, helper, db
from app.forms import LoginForm, UniformScoreSubmission, PerformanceScoreForm
from app.models import User, PerformanceCheckScores, UniformScores
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.helper import make_uniform_score_list


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    userid = current_user.get_id()
    return render_template('index.html', title='Home Page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/cadet', methods=['GET', 'POST'])
@login_required
def cadet():
    username = current_user.get_id()
    user = User.query.filter_by(id=username).first_or_404()
    if user.usertype.lower() == 'cadet':
        uniformScoresListAll = helper.make_uniform_score_list(user.uniformscores)
        uniformScoresList = uniformScoresListAll
        performance_score_list = helper.performance_score_list(user.performance_scores)
        return render_template('cadet.html', title=str(user.name), uniformScoresList=uniformScoresList,
                               performance_score_list=performance_score_list)
    else:
        # uniformScoresList = helper.make_uniform_score_list(user.uniformscores)
        # performance_score_list = helper.performance_score_list(user.performance_scores)
        # return render_template('cadet.html', title=str(user.name), uniformScoresList=uniformScoresList,
        #                        performance_score_list=performance_score_list)
        return render_template('index.html', title='Home Page')


@app.route('/officer', methods=['GET', 'POST'])
@login_required
def officer():
    username = current_user.get_id()
    user = User.query.filter_by(id=username).first_or_404()
    return render_template('officer.html', title='Admin', name=username)


@app.route('/adduniformscore', methods=['GET','POST'])
@login_required
def add_uni():
    username = current_user.get_id()
    user = User.query.filter_by(id=username).first_or_404()
    if user.usertype.lower() == 'cadet':
        return render_template('index.html', title='Home Page')
    else:
        form = UniformScoreSubmission()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.cadet_last_name.data).first()
            uniform_score = user.uniformscores[0]
            uniform_score.set_score(form.week.data, form.score.data)
            db.session.commit()
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        return render_template('adduniformscore.html', title='Record Uniform Score', form=form)

@app.route('/addperformancescore', methods=['GET','POST'])
@login_required
def add_performance():
    username = current_user.get_id()
    user = User.query.filter_by(id=username).first_or_404()
    if user.usertype.lower() == 'cadet':
        return render_template('index.html', title='Home Page')
    else:
        form = PerformanceScoreForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.cadet_last_name.data).first()
            performance_score = user.performance_scores[0]
            performance_score.set_score(form.performance.data, form.score.data)
            db.session.commit()
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        return render_template('/addperformancescore.html', title='Add a Performance Score', form=form)