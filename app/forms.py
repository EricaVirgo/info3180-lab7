from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename



class UploadForm(FlaskForm):
    
    description = TextAreaField('Description', validators = [InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'])])
    
    
    
