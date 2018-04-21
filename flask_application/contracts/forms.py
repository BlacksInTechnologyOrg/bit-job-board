from flask_wtf import FlaskForm
from flask_security.forms import Required
from wtforms import StringField, FieldList


class ContractForm(FlaskForm):
    title = StringField('Title', [Required()])
    type = FieldList(StringField('Type'))
    description = StringField('Description', [Required()])
