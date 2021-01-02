from app import app
from models import Snack, db

db.drop_all()
db.create_all()

Snack.query.delete()

cool_ranch = Snack(email="caleb@mail.com", name="Cool Ranch Doritos", category='chips', price=3.5, is_healthy=False, quantity=4, unit_measure="Ounces")
nacho_chz = Snack(email="caleb@mail.com", name="Nacho Cheese Doritos", category='chips', price=3.5, is_healthy=False, quantity=4, unit_measure="Ounces")
og_cheeto = Snack(email="caleb@mail.com",name="Crunchy Cheetos", category='chips', price=3.5, is_healthy=False, quantity=4, unit_measure="Ounces")

db.session.add(cool_ranch)
db.session.add(nacho_chz)
db.session.add(og_cheeto)

db.session.commit()