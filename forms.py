from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField
from wtforms.validators import InputRequired, Email, email_validator

class SnackForm(FlaskForm):
    """Form for adding snacks."""
    email = StringField("Email", validators=[Email(message="Please provide a valid email.")])
    name = StringField("Snack Name", validators=[InputRequired(message="Must provide a snack name.")])
    category = RadioField("Category", choices=[('candy', 'Candy'), ('chips', 'Chips'), ('hlth', 'Health Food'), ('etc', 'Et Cetera')])
    price = FloatField("Price in USD")
    is_healthy = BooleanField("Is this snack healthy?")
    quantity = IntegerField("Quantity")
    unit_measure = StringField("Unit of Measurement")