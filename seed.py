from app import app
from models import Snack, db

db.drop_all()
db.create_all()

Snack.query.delete()

cool_ranch = Snack(name="Cool Ranch Doritos", price=3.5)
nacho_chz = Snack(name="Nacho Cheese Doritos", price=3.5)
og_cheeto = Snack(name="Crunchy Cheetos", price=3.5)

db.session.add(cool_ranch)
db.session.add(nacho_chz)
db.session.add(og_cheeto)

db.session.commit()