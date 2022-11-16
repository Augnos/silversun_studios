from flask import render_template
from flask_app import app


# ---------- Home Page -----------
@app.route("/")
def home():
    return render_template('home.html', home=True)


# ---------- About Page -----------
@app.route("/about")
def about():
    return render_template('about.html', about=True)


# ---------- Studios Page -----------
@app.route("/studios")
def studios():
    return render_template('studios.html', studios=True)


# ---------- Services Page -----------
@app.route("/services")
def services():
    return render_template('services.html', services=True)


# ---------- FAQ Page -----------
@app.route("/faq")
def faq():
    return render_template('faq.html', faq=True)


# ---------- Availability Page -----------
@app.route("/availability")
def availability():
    return render_template('availability.html', availability=True)


# ---------- Booking Page -----------
@app.route("/booking")
def booking():
    return render_template('booking.html', booking=True)
