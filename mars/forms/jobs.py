from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    team_leader = TextAreaField("Team Leader id")
    work_size = TextAreaField("Work Size")
    collaborators = TextAreaField("Collaborators")
    is_finished = BooleanField("Is job finished?")
    submit = SubmitField("Submit")