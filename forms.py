from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField

class AddSnackForm(FlaskForm):
    """Form for adding snacks."""
    
    name = StringField("Snack Name")
    category = RadioField("Category", choices=[('candy', 'Candy'), ('chips', 'Chips'), ('hlth', 'Health Food'), ('etc', 'Et Cetera')])
    price = FloatField("Price in USD")
    is_healthy = BooleanField("Is this snack healthy?")
    quantity = IntegerField("Quantity")
    unit_measure = StringField("Unit of Measurement")