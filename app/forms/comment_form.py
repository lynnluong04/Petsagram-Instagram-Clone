from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField, Length
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    post_id = IntegerField("Post Id", validators=[DataRequired()])
    owner_id = IntegerField("Owner Id", validators=[DataRequired()])
    content = StringField("Content", validators=[DataRequired(), ])
    created_at = DateTimeField('created_at', format="%Y-%m-%d %H:%M:%S", validators=[DataRequired()])
