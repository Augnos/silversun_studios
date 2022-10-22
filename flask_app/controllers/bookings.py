from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.booking import Booking, studio_calendar

# # ---------- Bookings (all) Page -----------
# @app.route("/bookings")
# def bookings():
#     return render_template("bookings.html", all_bookings = Booking.select_all_bookings())


# # ---------- Bookings (one) Page -----------
# @app.route("/bookings/<id>")
# def bookings_one(id):
#     return render_template("show_booking.html", booking = Booking.get_one({"id":id}))


# ------------------------------------------------------
# -------------------- POST Routes ---------------------
# ------------------------------------------------------

# ---------- Insert New Booking Post -----------
@app.route('/insert/booking', methods=["POST"])
def insert_booking():
    data = {
        "start": {
            "dateTime": (str(request.form["date"]) + "T" + str(request.form["start_time"]) + ":00-07:00"),
            "timeZone": "America/Los_Angeles"
        },
        "end": {
            "dateTime": (str(request.form["date"]) + "T" + str(request.form["end_time"]) + ":00-07:00"),
            "timeZone": "America/Los_Angeles"
        },
        "summary": request.form["name"],
        'attendees': [
            {'email': request.form["email"]},
        ]
    }
    print(data)
    Booking.insert_booking(data, studio_calendar(request.form["studio"]))
    return redirect('/booking')


# # ---------- Update Booking Post -----------
# @app.route('/bookings/<id>/update', methods=["POST"])
# def edit_booking(id):
#     data = {
#         "id": id,
#         "name": request.form["name"],
#     }
#     Booking.update_booking(data)
#     return redirect('/')


# # ---------- Delete Booking Post -----------
# @app.route('/bookings/<id>/delete')
# def delete_booking(id):

#     data = {"id": id}
#     Booking.delete(data)
#     return redirect('/')


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
