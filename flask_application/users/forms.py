from flask_wtf import FlaskForm
from flask_security.forms import RegisterForm, Required
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField

class ExtendedRegisterForm(RegisterForm):
    username = StringField('Username', [Required()])
    first_name = StringField('First Name', [Required()])
    last_name = StringField('Last Name', [Required()])

class ProfilePicForm(FlaskForm):
    profilepic = FileField(validators=[FileAllowed(['jpg','png'], 'Picture Only!')])
