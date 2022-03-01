from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def main():
    db_session.global_init("db/data.db")
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == 1).first()
    jobs = Jobs(job="Личная запись", work_size=15,
                is_finished=True)
    user.jobs.append(jobs)
    db_sess.commit()


@app.route('/work_journal')
def work_journal():
    db_session.global_init("db/data.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template("jobs.html", jobs=jobs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')