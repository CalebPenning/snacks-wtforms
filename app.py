from flask import Flask, flash, redirect, render_template, session, request
from flask_debugtoolbar import DebugToolbarExtension
import datetime
from models import Snack, connect_db, db
from forms import AddSnackForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///snack_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'snacks'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/snacks/new', methods=["GET", "POST"])
def add_snack():
    print(request.form)
    form = AddSnackForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        flash(f"Created new snack: {name}, price of ${price}")
        return redirect('/')
    else:    
        return render_template("add_snack_form.html", form=form)

@app.route('/snacks/all')
def show_all_snacks():
    snacks = Snack.query.all()
    return render_template('all_snacks.html', snacks=snacks)