from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, validators
from wtforms.validators import ValidationError


class EmployeeSearchForm(FlaskForm):

    department = SelectField("department")
    name = StringField("Search")
    from_birthday = DateField("Start date", validators=(validators.Optional(),))
    to_birthday = DateField("End date", validators=(validators.Optional(),))
    submit = SubmitField("Search")

    def validate_from_birthday(self, from_birthday):
        if self.to_birthday.data and from_birthday.data:
            if from_birthday.data > self.to_birthday.data:
                raise ValidationError("Start date is bigger than end date")