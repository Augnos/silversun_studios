from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.booking import Booking


# -----------------------------------------------------
# -------------------- GET Routes ---------------------
# -----------------------------------------------------

# ---------- Home Page -----------
@app.route("/")
def get_home():
    return render_template('home.html')

# ---------- About Page -----------
@app.route("/about")
def get_about():
    return render_template('about.html')

# ---------- Studios Page -----------
@app.route("/studios")
def get_studios():
    return render_template('studios.html')

# ---------- Services Page -----------
@app.route("/services")
def get_services():
    return render_template('services.html')

# ---------- FAQ Page -----------
@app.route("/faq")
def get_faq():
    return render_template('faq.html')

# ---------- Availability Page -----------
@app.route("/availability")
def get_availability():
    return render_template('availability.html')

# ---------- Booking Page -----------
@app.route("/booking")
def get_booking():
    return render_template('booking.html')


# ---------- Bookings (all) Page -----------
@app.route("/bookings")
def bookings():
    return render_template("bookings.html", all_bookings = Booking.select_all_bookings())


# ---------- Bookings (one) Page -----------
@app.route("/bookings/<id>")
def bookings_one(id):
    return render_template("show_booking.html", booking = Booking.get_one({"id":id}))


# ------------------------------------------------------
# -------------------- POST Routes ---------------------
# ------------------------------------------------------

# ---------- Insert New Booking Post -----------
@app.route('/insert/booking', methods=["POST"])
def insert_booking():
    data = {
        "name": request.form["name"],
    }
    Booking.insert_new_booking(data)
    return redirect('/')


# ---------- Update Booking Post -----------
@app.route('/bookings/<id>/update', methods=["POST"])
def edit_booking(id):
    data = {
        "id": id,
        "name": request.form["name"],
    }
    Booking.update_booking(data)
    return redirect('/')


# ---------- Delete Booking Post -----------
@app.route('/bookings/<id>/delete')
def delete_booking(id):

    data = {"id": id}
    Booking.delete(data)
    return redirect('/')


# # ---------- Bcrypt Password Post -----------
# @app.route('/register/user', methods=['POST'])
# def register():
#     # validate the form here ...
#     # create the hash
#     pw_hash = bcrypt.generate_password_hash(request.form['password'])
#     print(pw_hash)
#     # put the pw_hash into the data dictionary
#     data = {
#         "username": request.form['username'],
#         "password" : pw_hash
#     }
#     # Call the save @classmethod on User
#     user_id = User.save(data)
#     # store user id into session
#     session['user_id'] = user_id
#     return redirect("/dashboard")