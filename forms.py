from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length


class AssignmentForm(FlaskForm):
    assignmtInfo = StringField('Assignment Info', validators=[DataRequired(), Length(min=-1, max=100, message='You cannot have more than 100 characters')])
    assignmtClass = SelectField('Class', validators=[DataRequired()], choices=[('Advanced Math','Advanced Math'), ('Anderson Bible', 'Anderson Bible'), ('Carpenter Bible', 'Carpenter Bible'), ('Rainear Bible', 'Rainear Bible'), ('AP History', 'AP History'), ('AP Psych', 'AP Psych'), ('Chemistry', 'Chemistry'), ('Smart English', 'Smart English'), ('Dumb English', 'Dumb English'), ('Coding I', 'Coding I'), ('Forensic Science', 'Forensic Science'), ('American Sign Language', 'American Sign Language'), ('ELS Prepworks', 'ELS Prepworks'), ('Class Party', 'Class Party')])
    #assignmtClass = SelectField('Class', validators=[DataRequired()], choices=[('Advanced Math','Anderson Bible','Carpenter Bible','Rainear Bible','AP History','AP Psychology','Chemistry','Smart English','Dumb English','Coding I','Forensic Science','American Sign Langauge','ELS Prepworks','Class Party')])
    assignmtDate = DateField('Due Date', validators=[DataRequired()])