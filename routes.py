import json
from app import app, db
from models import  User

from flask import render_template,\
    flash,\
    redirect,\
    url_for
    
from flask import session

from forms import LoginForm, RegisterForm

@app.route('/')
@app.route('/index/')
def index():
    if session.get('is_auth'):
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('is_auth'):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query\
            .filter_by(login = form.login.data)\
            .first()
        if user is not None and user.password == form.password.data:
            flash(f'Login {form.login.data}')
            session['is_auth'] = True
            return redirect(url_for('index'))
        flash(f'Такого користувача не існує {form.login.data}')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('is_auth'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            login = form.login.data,
            password =  form.password.data
        )
        db.session.add(user)
        try:
            db.session.commit()
            flash(f'Registered {form.login.data}')
            return redirect(url_for('login'))
        except:
            db.session.rollback()
            flash(f'Такий користувач вже зареєстрований: {form.login.data}!')     
        
    return render_template('register.html', form=form)
