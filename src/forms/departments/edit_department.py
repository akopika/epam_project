"""
This module implements instance of edit department profile web form
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from src.rest.api_controllers import DepartmentApiController


class EditDepartmentForm(FlaskForm):
    """
    Custom FlaskForm object for register department form.
    :param uuid: uuid of edited department
    """
    name = StringField("Department name", validators=[DataRequired()])
    submit = SubmitField("Edit Profile")

    def __init__(self, uuid: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uuid = uuid

    def validate_name(self, name):
        """
        validator for department name field
        :param name: department name string field
        :raise ValidationError: if input name already existed in database
        """
        departments = DepartmentApiController.get_all_departments()
        edited_department = DepartmentApiController.get_department_by_uuid(self.uuid)
        names = [department["name"] for department in departments]
        if name.data in names and name.data.strip() != edited_department["name"].strip():
            raise ValidationError("Department with this name is already exists")
